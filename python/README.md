# Solana Transaction Parser

Python bindings for parsing Solana transactions using a Go-based C shared library.

## Installation

```bash
pip install solana-tx-parser
```

## Usage

```python
from solana_tx_parser import parse_transaction

tx_json = '...'  # Your transaction JSON string
result = parse_transaction(tx_json)
```

result is a list of transaction objects:

```python
[
    {
        "rawTx": {...},  # raw transaction data
        "accountList": [
            "H9m6fFpfGupwiJAY2aKd9d2MQe1StYSwxRNPcx2NHQuX",
            "BgMff4ZEtg6Apu83cHxiPZBioDmEusphusWwV1Jtk9nj",
            "CebN5WGQ4jvEPvsVU4EoHEpgzq1VV7AbicfhtW4xC9iM",
            "TEf2o4WuA8RjzGK5SoE6kPLQzQE4gjrgp4tvErURicA",
            "8DCJfMMoHXCZZhVfnAy8f5zydcnV23CQ5UR63gasX1yh",
            "ComputeBudget111111111111111111111111111111",
            "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL",
            "8suSDnKVFRyAsTpZ7e2J2seofy6fVhL3cerTfyYppump",
            "11111111111111111111111111111111",
            "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
            "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P",
            "4wTV1YmiEkRvAtNtsSGPtUrqRYQMe5SKy2uB4Jjaxnjf",
            "SysvarRent111111111111111111111111111111111",
            "Ce6TQqeHC9p8KetsN6JsjHK7UTZk7nasjjnr7XxXp9F1"
        ],
        "actions": [
            {
                "programId": "ComputeBudget111111111111111111111111111111",
                "programName": "ComputeBudget",
                "instructionName": "SetComputeUnitLimit",
                "computeUnitLimit": 250000
            },
            {
                "programId": "ComputeBudget111111111111111111111111111111",
                "programName": "ComputeBudget",
                "instructionName": "SetComputeUnitPrice",
                "microLamports": 1000000
            },
            {
                "programId": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL",
                "programName": "Unknown",
                "instructionName": "Unknown",
                "error": null
            },
            {
                "programId": "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P",
                "programName": "PumpFun",
                "instructionName": "Buy",
                "who": "H9m6fFpfGupwiJAY2aKd9d2MQe1StYSwxRNPcx2NHQuX",
                "fromToken": "So11111111111111111111111111111111111111112",
                "fromTokenAmount": 279965,
                "toToken": "8suSDnKVFRyAsTpZ7e2J2seofy6fVhL3cerTfyYppump",
                "toTokenAmount": 10000000000,
                "feeAmount": 2799
            }
        ]
    }
]
```
