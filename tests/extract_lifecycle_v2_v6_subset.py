#!/usr/bin/env python3
"""从 test_lifecycle_bundle.sh 抽出所有 *-lifecycle-vN (N>=2)* 段落。"""
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SRC = SCRIPT_DIR / "test_lifecycle_bundle.sh"
DEST = SCRIPT_DIR / "test_lifecycle_v2_v6_subset.sh"

VERSION_RE = re.compile(r"-lifecycle-v(\d+)$")


def main():
    content = SRC.read_text(encoding="utf-8")
    pat = re.compile(r"(?m)^(# -- .+ --)\s*\n")
    parts = pat.split(content)
    preamble = parts[0].rstrip()
    out = [
        preamble,
        "",
        "# Subset: lifecycle tests whose name ends with -lifecycle-vN (N >= 2)",
        "",
    ]
    count = 0
    for i in range(1, len(parts), 2):
        if i + 1 >= len(parts):
            break
        header = parts[i]
        body = parts[i + 1]
        m = re.match(r"# -- (.+) --", header)
        if not m:
            continue
        vm = VERSION_RE.search(m.group(1).strip())
        if vm and int(vm.group(1)) >= 2:
            out.append(header)
            out.append(body.rstrip("\n"))
            count += 1
    text = "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    DEST.write_text(text, encoding="utf-8")
    cmds = sum(1 for line in text.splitlines() if line.strip().startswith("awscli "))
    print(f"Wrote {DEST.name}: {count} sections, {cmds} awscli commands")


if __name__ == "__main__":
    main()
