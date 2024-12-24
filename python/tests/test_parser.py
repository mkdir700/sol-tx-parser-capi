import json
from pathlib import Path

import pytest

from solana_tx_parser import parse_transaction

cur = Path(__file__).parent
examples = cur / "examples"


# 使用 pytest 从 examples 目录下读取所有的 json 文件，并且测试每个文件的解析结果
@pytest.mark.parametrize("file", examples.glob("*.json"))
def test_parse_transaction(file):
    with open(file, "r") as f:
        sample_tx = f.read()

    data = json.loads(sample_tx)
    if "id" not in data:
        data = {"jsonrpc": "2.0", "result": data, "id": 0}

    result = parse_transaction(json.dumps(data))
    try:
        assert result is not None
        assert result[0]["actions"] is not None
    finally:
        print(f"Failed to parse {file.name}")
