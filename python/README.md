# Solana Transaction Parser

Python bindings for parsing Solana transactions using a Go-based C shared library.

## Installation

```bash
pip install git+https://github.com/mkdir700/sol-tx-parser-capi.git#subdirectory=python
```

## Usage

```python
from solana_tx_parser import parse_transaction

tx_json = '...'  # Your transaction JSON string
result = parse_transaction(tx_json)
```
