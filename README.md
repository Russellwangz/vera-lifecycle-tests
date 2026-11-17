# Vera Lifecycle Tests

Beyond the official AWS CLI documentation examples, this repository holds two evaluation suites for the EC2 emulator in [Vera](https://github.com/project-vera/vera) (`emulators/aws-ec2`). Vera here only implements EC2, so every runnable line is either an EC2 command or an EC2 stand-in for a command that originally called another service.

## Scraped AWS CLI

The first suite is scraped from real AWS CLI usage in **16 public GitHub repositories** (shell, Python, and similar scripts), not from the single-flag examples in the AWS CLI docs.

How a command gets into the suite:

1. Clone the repositories.
2. Scan script files for `aws ...` lines, including commands split across lines with `\`.
3. Record the command together with the repository and file it came from.
4. Classify it by service.
   - Service is `ec2`: keep the command and label it `ec2`. It runs as scraped.
   - Service is anything else (IAM, ELB, SSM, STS, CloudWatch, `aws configure`, and so on): keep the original line and label it `non-ec2`, so the real call is still visible.
5. For each `non-ec2` line, add one more command that calls only EC2 and has a similar purpose. Label that line `augmented-ec2`. When the original script calls a non-EC2 service, the extra EC2 command lets the same script still run on an emulator that only implements EC2.

`tests/test_labeled.sh` is that result: **142 commands**. **116** are labeled `ec2`. **13** `non-ec2` calls (IAM, ELB, SSM, STS, CloudWatch, `aws configure`, and similar) are each paired with an `augmented-ec2` stand-in. The GitHub-sourced section of that file is numbered **TC01–TC60**, from the 16 repositories listed in the file header.

Example, TC56: a script looked up the latest Amazon Linux AMI through SSM Parameter Store. The original call stays, and the EC2 stand-in lists Amazon-owned AMIs instead.

```bash
# label: non-ec2
awscli ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --region us-east-1
# label: augmented-ec2
awscli ec2 describe-images --owners amazon --filters 'Name=name,Values=amzn2-ami-hvm-*' 'Name=state,Values=available' --query 'Images[:1].ImageId' --output text
```

These cases are not single-flag examples. They use tag and VPC filters, JMESPath `--query` projections over nested fields (security-group rules, routes, instance placement), and multi-command setups where a later step depends on an earlier one.

Related files:

- `tests/augment_prompt.md` — the prompt used to draft an EC2-only stand-in for each non-EC2 line.
- `tests/print_commands_with_endpoint.py` and `tests/utils/parse_aws_commands.py` — read RST examples and print the same labeled `awscli` lines (`ec2`, `non-ec2`, `augmented-ec2`).

## Lifecycle tests

The second suite chains one resource through its whole life, instead of running each CLI call in isolation:

**create → describe → modify → describe → delete → describe (confirm it is gone)**

There are two layers. They use the same shape.

### Hand-written scenarios

`tests/test_lifecycle.py` has **25 hand-written scenarios** (VPC, subnet, security group, volume, instance, transit gateway, and others). Each function:

1. Creates any prerequisite in the same scenario (a VPC before a subnet, two VPCs before a peering connection).
2. Runs create, then describe, and checks the fields that were requested.
3. Modifies the resource, describes it again, and checks that the new value stuck.
4. Deletes it, describes it again, and checks that it is gone.
5. Deletes the prerequisites.

### Generated scenarios

`tests/generate_lifecycle_rsts.py` turns the same kind of chain into AWS-docs-style RST and a bash bundle.

1. Each entry in `LIFECYCLE_TESTS` is one scenario: an ordered list of steps that share one placeholder ID, such as `vpc-0a60eb65b4EXAMPLE` or `vol-1234567890abcdef0`.
2. The generator writes `tests/cli/ec2/<name>-lifecycle.rst` in documentation form (example title, `aws ec2 ...` command, and the create output that contains the placeholder ID).
3. It writes the same steps, in the same order, into `tests/test_lifecycle_bundle.sh`. Each scenario is marked `# -- <name> --`, and each command is marked `# label: lifecycle-file:<name>`.
4. A modify variant keeps the same create and delete and only changes the middle step. Volumes alone are split that way: resize, volume type, IOPS, throughput, combined type/IOPS/size, and `modify-volume-attribute` (`volume-lifecycle-v2` through `volume-lifecycle-v7`).

`tests/cli/ec2` contains **79 lifecycle RST files**: **53** resource types, plus **26** modify-variant files. `LIFECYCLE_TESTS` writes **71** of those scenarios into RST and into `tests/test_lifecycle_bundle.sh` (**386** commands), across VPCs, subnets, volumes, instances, security groups, gateways, transit gateways, and related resources. Eight RST files are in the tree and are not entries in the generator or the bundle: `customer-gateway-lifecycle`, `network-interface-lifecycle`, `placement-group-lifecycle`, `volume-lifecycle`, `vpc-endpoint-lifecycle`, `vpc-endpoint-service-lifecycle`, `vpc-lifecycle`, and `vpc-peering-connection-lifecycle`. The hand-written suite still covers those resources.

One volume chain looks like this. Every step after create uses the same placeholder volume ID:

```text
aws ec2 create-volume --volume-type gp3 --size 100 --availability-zone us-east-1a
aws ec2 describe-volumes --volume-ids vol-1234567890abcdef0
aws ec2 modify-volume --volume-id vol-1234567890abcdef0 --size 150
aws ec2 describe-volumes --volume-ids vol-1234567890abcdef0
aws ec2 delete-volume --volume-id vol-1234567890abcdef0
```

### How a generated scenario is run

`tests/eval_emulator.py --lifecycle` is what ties the placeholder IDs to the emulator.

1. Commands run in file order.
2. A new `# label: lifecycle-file:...` starts a new scenario and clears the ID map, so one scenario cannot leak IDs into the next.
3. After a successful create, the real ID is read from the JSON response (`vpc-...`, `vol-...`, `eipalloc-...`) and stored by prefix.
4. Before the next command in that scenario, placeholders such as `vpc-0a60eb65b4EXAMPLE` are rewritten to that real ID. Describe, modify, and delete then hit the resource that was just created.
5. After create, modify, and delete, a follow-up describe checks that modified fields stuck and that delete actually removed the resource.

`tests/extract_lifecycle_v2_v6_subset.py` copies every `*-lifecycle-vN` section with N ≥ 2, including `volume-lifecycle-v7`, into `tests/test_lifecycle_v2_v6_subset.sh` (26 scenarios). `tests/run_lifecycle_v2_v6_subset.sh` runs that subset with `--lifecycle`.

## Run

Start the Vera EC2 emulator (default `http://localhost:5003`) and use the `awscli` wrapper from that checkout. The wrapper sends AWS CLI calls to the emulator.

```bash
cd /path/to/vera/emulators/aws-ec2
bash install.sh
uv run main.py
```

In another shell:

```bash
export PATH="/path/to/vera/emulators/aws-ec2/.venv/bin:$PATH"
cd /path/to/vera-lifecycle-tests/tests

# Generated lifecycle bundle. Placeholder IDs are replaced from create responses.
python eval_emulator.py test_lifecycle_bundle.sh --lifecycle

# Modify-variant subset only.
./run_lifecycle_v2_v6_subset.sh

# Hand-written scenarios. -k selects by name, for example vpc or volume.
python test_lifecycle.py
python test_lifecycle.py -k vpc

# Scraped CLI, including non-ec2 lines and their augmented-ec2 stand-ins.
python eval_emulator.py test_labeled.sh
```

Regenerate the RST files and the bundle from the definitions in the generator:

```bash
python generate_lifecycle_rsts.py
python extract_lifecycle_v2_v6_subset.py
```
