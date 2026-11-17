#!/usr/bin/env python3
"""
Script to print AWS CLI commands for testing.
Parses RST files from cli directory and outputs them with either:
- awscli wrapper (default)
- --endpoint-url for LocalStack (--ls flag)
"""

import sys
from pathlib import Path
from utils.parse_aws_commands import parse_aws_commands, parse_aws_commands_from_directory


def add_endpoint_to_command(cmd, endpoint_url):
    """
    Add endpoint URL to an AWS CLI command.
    Inserts --endpoint-url after 'aws' and before the service name.
    
    Example:
        Input: "aws ec2 describe-instances --region us-east-1"
        Output: "aws --endpoint-url=http://localhost:4566 ec2 describe-instances --region us-east-1"
    """
    if not cmd.startswith('aws '):
        return cmd
    
    # Split at 'aws ' and insert endpoint after it
    rest_of_cmd = cmd[4:]  # Remove 'aws '
    return f"aws --endpoint-url={endpoint_url} {rest_of_cmd}"


def to_awscli_command(cmd):
    """
    Convert an 'aws ...' command to use the awscli wrapper.

    Example:
        Input:  "aws ec2 describe-instances --region us-east-1"
        Output: "awscli ec2 describe-instances --region us-east-1"
    """
    if not cmd.startswith('aws '):
        return cmd
    return f"awscli {cmd[4:]}"


def is_ec2_command(cmd):
    """Return True if the command targets the EC2 service (aws ec2 ... or awscli ec2 ...)."""
    s = cmd.strip()
    if s.startswith("aws "):
        rest = s[4:].lstrip()
        return rest.startswith("ec2 ")
    if s.startswith("awscli "):
        rest = s[7:].lstrip()
        return rest.startswith("ec2 ")
    return False


def get_augmented_ec2_placeholder(use_localstack=False, endpoint_url=None):
    """Return a minimal EC2 command usable as placeholder for augmented-ec2."""
    cmd = "aws ec2 describe-vpcs --query 'Vpcs[].VpcId' --output text"
    if use_localstack:
        return add_endpoint_to_command(cmd, endpoint_url)
    return to_awscli_command(cmd)


def print_commands(data, include_id=None, include_file=None, use_localstack=False, endpoint_url=None,
                   label=False, augmented_map=None):
    """
    Print commands from parsed data.

    Args:
        data: Dictionary of parsed commands from parse_aws_commands_from_directory
        include_id: Include commands that require ID parameters
        include_file: Include commands that require file:// parameters
        use_localstack: If True, add --endpoint-url for LocalStack
        endpoint_url: Endpoint URL to use (only when use_localstack=True)
        label: If True, emit "# label: ec2" or "# label: non-ec2" and "# label: augmented-ec2" before commands
        augmented_map: Optional dict mapping original non-ec2 command -> augmented EC2-only command for label mode
    """
    total_commands = 0
    printed_commands = 0
    augmented_map = augmented_map or {}

    for file_path, commands in data.items():
        for cmd_data in commands:
            total_commands += 1

            # Apply include filters if specified
            if cmd_data['use_id'] and not include_id:
                continue
            if cmd_data['use_file'] and not include_file:
                continue

            raw_cmd = cmd_data['cmd']
            if use_localstack:
                out_cmd = add_endpoint_to_command(raw_cmd, endpoint_url)
            else:
                out_cmd = to_awscli_command(raw_cmd)

            if label:
                if is_ec2_command(raw_cmd):
                    print("# label: ec2")
                    print(out_cmd)
                else:
                    print("# label: non-ec2")
                    print(out_cmd)
                    print("# label: augmented-ec2")
                    aug = augmented_map.get(raw_cmd) or get_augmented_ec2_placeholder(
                        use_localstack=use_localstack, endpoint_url=endpoint_url
                    )
                    print(aug)
            else:
                print(out_cmd)
            printed_commands += 1

    # Print summary to stderr so it doesn't interfere with command output
    print(f"\n# Total commands: {total_commands}", file=sys.stderr)
    print(f"# After filtering: {printed_commands}", file=sys.stderr)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Print AWS CLI commands for testing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate commands for emulator (using awscli wrapper)
  python print_commands_with_endpoint.py > test.sh

  # Generate commands for LocalStack
  python print_commands_with_endpoint.py --ls > test_ls.sh

  # Generate commands for LocalStack with custom endpoint
  python print_commands_with_endpoint.py --ls --endpoint http://localhost:4566 > test_ls.sh

  # Include commands with ID parameters
  python print_commands_with_endpoint.py --include-id > test.sh

  # Only one RST file (e.g. github_ec2_tests.rst)
  python print_commands_with_endpoint.py --cli-file cli/ec2/Russell_Public_testcases/github_ec2_tests.rst --include-id 2>/dev/null > test_github_ec2.sh

  # With labels (ec2 / non-ec2 / augmented-ec2) and optional LLM-generated augment file
  python print_commands_with_endpoint.py -d cli/ec2/Russell_Public_testcases --include-id --label > test_labeled.sh
  python print_commands_with_endpoint.py -d cli/ec2/Russell_Public_testcases --include-id --label --augmented-file augmented_ec2.txt > test_labeled.sh
        """
    )

    parser.add_argument(
        '--label',
        '-L',
        action='store_true',
        help='Add # label: ec2 | non-ec2 | augmented-ec2 before each command; non-ec2 get a placeholder augmented line (override with --augmented-file)'
    )

    parser.add_argument(
        '--augmented-file',
        default=None,
        help='File of LLM-generated augmented EC2 commands (one per line, same order as non-ec2 commands) to use for augmented-ec2 lines'
    )

    parser.add_argument(
        '--cli-file',
        '-f',
        default=None,
        help='Single RST file to parse (overrides --cli-dir when set)'
    )

    parser.add_argument(
        '--cli-dir',
        '-d',
        default='cli',
        help='Path to CLI directory with RST files (default: cli)'
    )

    parser.add_argument(
        '--exclude-file',
        action='append',
        default=[],
        help='Exclude RST file by name when using --cli-dir (can be repeated)'
    )

    parser.add_argument(
        '--ls',
        action='store_true',
        help='Generate commands for LocalStack (adds --endpoint-url)'
    )

    parser.add_argument(
        '--endpoint',
        '-e',
        default='http://localhost:4566',
        help='Endpoint URL for LocalStack (default: http://localhost:4566)'
    )

    parser.add_argument(
        '--include-file',
        action='store_true',
        help='Include commands that use file parameters'
    )

    parser.add_argument(
        '--include-id',
        action='store_true',
        help='Include commands that use ID parameters'
    )

    args = parser.parse_args()

    mode = "LocalStack" if args.ls else "Emulator (awscli wrapper)"
    print(f"Mode: {mode}", file=sys.stderr)
    if args.ls:
        print(f"Endpoint: {args.endpoint}", file=sys.stderr)

    if args.cli_file:
        # Single file: parse only that RST
        cli_file = Path(args.cli_file)
        if not cli_file.is_absolute():
            cli_file = (Path.cwd() / cli_file).resolve()
        if not cli_file.exists():
            print(f"Error: CLI file not found: {cli_file}", file=sys.stderr)
            sys.exit(1)
        print(f"Parsing single RST file: {cli_file}", file=sys.stderr)
        commands = parse_aws_commands(cli_file)
        data = {cli_file.name: commands} if commands else {}
    else:
        # Directory: parse all RST under cli_dir
        cli_dir = Path(args.cli_dir)
        if not cli_dir.exists():
            print(f"Error: CLI directory not found: {cli_dir}", file=sys.stderr)
            print(f"Please ensure the directory exists or specify with --cli-dir", file=sys.stderr)
            sys.exit(1)
        print(f"Parsing RST files from: {cli_dir}", file=sys.stderr)
        data = parse_aws_commands_from_directory(cli_dir, quiet=True)
        if args.exclude_file:
            exclude = {name.strip() for name in args.exclude_file if name and name.strip()}
            if exclude:
                data = {k: v for k, v in data.items() if Path(k).name not in exclude}

    if not data:
        src = args.cli_file or args.cli_dir
        print(f"Error: No commands found in {src}", file=sys.stderr)
        sys.exit(1)

    total_in_data = sum(len(cmds) for cmds in data.values())
    print(f"Found {len(data)} file(s) with {total_in_data} commands", file=sys.stderr)
    print("", file=sys.stderr)  # Blank line for readability

    # Collect ordered list of non-ec2 commands for label mode (for augment prompt / augmented-file)
    ordered_non_ec2 = []
    if args.label:
        for file_path, commands in data.items():
            for cmd_data in commands:
                if cmd_data['use_id'] and not args.include_id:
                    continue
                if cmd_data['use_file'] and not args.include_file:
                    continue
                if not is_ec2_command(cmd_data['cmd']):
                    ordered_non_ec2.append(cmd_data['cmd'])
        if ordered_non_ec2:
            out_dir = Path.cwd()
            non_ec2_path = out_dir / "non_ec2_commands_for_augment.txt"
            prompt_path = out_dir / "augment_prompt.md"
            non_ec2_path.write_text("\n".join(ordered_non_ec2) + "\n", encoding="utf-8")
            prompt_path.write_text(
                "Below are AWS CLI commands that use services other than EC2 (e.g. IAM, ELB, SSM).\n"
                "For each command, output a single replacement line that uses only the EC2 service and is valid for testing against an EC2 emulator.\n"
                "Strip or replace non-EC2 parts; you may use generic EC2 calls (e.g. describe-vpcs, describe-instances) where no direct EC2 equivalent exists.\n"
                "Output exactly one line per input line, in the same order. Each line should be a complete 'aws ec2 ...' command.\n\n"
                "Input commands (one per line):\n"
                "---\n" + "\n".join(ordered_non_ec2) + "\n---\n\n"
                "Output (one EC2-only command per line, same order):\n",
                encoding="utf-8"
            )
            print(f"# Non-EC2 commands ({len(ordered_non_ec2)}) written to {non_ec2_path}", file=sys.stderr)
            print(f"# LLM prompt written to {prompt_path} (run LLM, save reply to augmented_ec2.txt, then pass --augmented-file augmented_ec2.txt)", file=sys.stderr)

    # Build augmented_map if --augmented-file given and --label
    augmented_map = {}
    if args.label and args.augmented_file and ordered_non_ec2:
        aug_path = Path(args.augmented_file)
        if aug_path.is_absolute():
            aug_path = aug_path
        else:
            aug_path = (Path.cwd() / aug_path).resolve()
        if aug_path.exists():
            aug_lines = [line.rstrip() for line in aug_path.read_text(encoding='utf-8').splitlines() if line.strip()]
            for i, raw in enumerate(ordered_non_ec2):
                if i < len(aug_lines):
                    aug = aug_lines[i]
                    if not aug.startswith('aws ') and not aug.startswith('awscli '):
                        aug = to_awscli_command(f"aws {aug}") if not args.ls else add_endpoint_to_command(f"aws {aug}", args.endpoint)
                    elif aug.startswith('aws ') and not args.ls:
                        aug = to_awscli_command(aug)
                    elif aug.startswith('aws ') and args.ls:
                        aug = add_endpoint_to_command(aug, args.endpoint)
                    augmented_map[raw] = aug
            if len(aug_lines) != len(ordered_non_ec2):
                print(f"# Augmented file has {len(aug_lines)} lines, non-ec2 count is {len(ordered_non_ec2)}", file=sys.stderr)
        else:
            print(f"Warning: augmented file not found: {aug_path}", file=sys.stderr)

    # Print commands
    print_commands(data, args.include_id, args.include_file, args.ls, args.endpoint,
                   label=args.label, augmented_map=augmented_map if args.label else None)


if __name__ == "__main__":
    main()
