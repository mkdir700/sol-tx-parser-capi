from solana_tx_parser import parse_transaction


def test_parse_transaction():
    sample_tx = '''{"jsonrpc":"2.0","result":{"slot":303139093,"transaction":{"signatures":["3eNYyuFzJrqXwdC4VnZQpRRqv4nvgEf4U1jrQEmTVDgoTEx9aNJEPM3BcNAVTcw3bMHCyYAQVJfhpyXoyLPBFLA8"],"message":{"header":{"numRequiredSignatures":1,"numReadonlySignedAccounts":0,"numReadonlyUnsignedAccounts":9}}}}}'''
    
    result = parse_transaction(sample_tx)
    assert result is not None
