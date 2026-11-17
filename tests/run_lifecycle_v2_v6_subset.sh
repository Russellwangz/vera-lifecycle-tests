#!/usr/bin/env bash
# 仅运行名字以 -lifecycle-v2..-lifecycle-v6 结尾的 14 个 lifecycle 用例（81 条 awscli 命令）。
# 需先启动模拟器: cd ../.. && uv run main.py   （默认 http://localhost:5003）
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
export PATH="$SCRIPT_DIR/../.venv/bin:$PATH"
exec python3 eval_emulator.py test_lifecycle_v2_v6_subset.sh --lifecycle "$@"
