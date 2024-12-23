import ctypes
import json
import os
import platform
from typing import Any, Dict, List


def _get_lib_path():
    system = platform.system()
    lib_dir = os.path.join(os.path.dirname(__file__), "lib")

    if system == "Darwin":  # macOS
        return os.path.join(lib_dir, "libsoltxparser.dylib")
    elif system == "Linux":  # Linux
        return os.path.join(lib_dir, "libsoltxparser.so")
    elif system == "Windows":  # Windows
        return os.path.join(lib_dir, "soltxparser.dll")
    else:
        raise OSError(f"Unsupported operating system: {system}")


# Get the library path
_lib_path = _get_lib_path()

# Load the shared library
_lib = ctypes.CDLL(_lib_path)


class ParseResult(ctypes.Structure):
    _fields_ = [("error", ctypes.c_char_p), ("result", ctypes.c_char_p)]


# Set function argument and return types
_lib.ParseTransaction.argtypes = [ctypes.c_char_p]
_lib.ParseTransaction.restype = ParseResult
_lib.FreeParseResult.argtypes = [ParseResult]


def parse_transaction(tx_data: str) -> List[Dict[str, Any]]:
    """Parse a Solana transaction.

    Args:
        tx_data: The transaction data as a string

    Returns:
        A dictionary containing the parsed transaction data

    Raises:
        RuntimeError: If parsing fails
    """
    result = _lib.ParseTransaction(tx_data.encode("utf-8"))

    try:
        if result.error:
            raise RuntimeError(result.error.decode("utf-8"))

        if result.result:
            return json.loads(result.result.decode("utf-8"))

        raise RuntimeError("No result and no error")

    finally:
        _lib.FreeParseResult(result)


if __name__ == "__main__":
    content = """
    {"jsonrpc":"2.0","result":{"slot":303139093,"transaction":{"signatures":["3eNYyuFzJrqXwdC4VnZQpRRqv4nvgEf4U1jrQEmTVDgoTEx9aNJEPM3BcNAVTcw3bMHCyYAQVJfhpyXoyLPBFLA8"],"message":{"header":{"numRequiredSignatures":1,"numReadonlySignedAccounts":0,"numReadonlyUnsignedAccounts":9},"accountKeys":["H9m6fFpfGupwiJAY2aKd9d2MQe1StYSwxRNPcx2NHQuX","BgMff4ZEtg6Apu83cHxiPZBioDmEusphusWwV1Jtk9nj","CebN5WGQ4jvEPvsVU4EoHEpgzq1VV7AbicfhtW4xC9iM","TEf2o4WuA8RjzGK5SoE6kPLQzQE4gjrgp4tvErURicA","8DCJfMMoHXCZZhVfnAy8f5zydcnV23CQ5UR63gasX1yh","ComputeBudget111111111111111111111111111111","ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL","8suSDnKVFRyAsTpZ7e2J2seofy6fVhL3cerTfyYppump","11111111111111111111111111111111","TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA","6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P","4wTV1YmiEkRvAtNtsSGPtUrqRYQMe5SKy2uB4Jjaxnjf","SysvarRent111111111111111111111111111111111","Ce6TQqeHC9p8KetsN6JsjHK7UTZk7nasjjnr7XxXp9F1"],"recentBlockhash":"C5qJoMm4oEd4NH8f19wF8nGwFKvEx18awZ36Fm96VTVp","instructions":[{"programIdIndex":5,"accounts":[],"data":"HnkkG7","stackHeight":null},{"programIdIndex":5,"accounts":[],"data":"3QCwqmHZ4mdq","stackHeight":null},{"programIdIndex":6,"accounts":[0,1,0,7,8,9],"data":"","stackHeight":null},{"programIdIndex":10,"accounts":[11,2,7,3,4,1,0,8,9,12,13,10],"data":"AJTQ2h9DXrBdFY6uXSvVBBH6MbT4sCDYK","stackHeight":null}],"addressTableLookups":[]}},"meta":{"err":null,"status":{"Ok":null},"fee":255000,"preBalances":[103494654,0,357369713798981,21192140,2039280,1,731913600,1461600,1,934087680,1141440,58530000,1009200,40000000],"postBalances":[100917610,2039280,357369713801780,21472105,2039280,1,731913600,1461600,1,934087680,1141440,58530000,1009200,40000000],"innerInstructions":[{"index":2,"instructions":[{"programIdIndex":9,"accounts":[7],"data":"84eT","stackHeight":2},{"programIdIndex":8,"accounts":[0,1],"data":"11119os1e9qSs2u7TsThXqkBSRVFxhmYaFKFZ1waB2X7armDmvK3p5GmLdUxYdg3h7QSrL","stackHeight":2},{"programIdIndex":9,"accounts":[1],"data":"P","stackHeight":2},{"programIdIndex":9,"accounts":[1,7],"data":"6dHTmbTMTZm6mynG47jWxdbTjuXbGJHiefLYF7XiBaZLV","stackHeight":2}]},{"index":3,"instructions":[{"programIdIndex":9,"accounts":[4,1,3],"data":"3DcCptZte3oM","stackHeight":2},{"programIdIndex":8,"accounts":[0,3],"data":"3Bxs4TANYoswz4Y7","stackHeight":2},{"programIdIndex":8,"accounts":[0,2],"data":"3Bxs4gqdzcC6NtK9","stackHeight":2},{"programIdIndex":10,"accounts":[13],"data":"2K7nL28PxCW8ejnyCeuMpbWojoBGexZs7tN3VavtnHif2axb1WwWnUMCTFK2UYA5QeYGR7fpUNLgjSWNKXt4AdbD3B3V44CneMw99Ni6EtaAQGbLbQr6rwNgWtUu5UAcaASx7tLf8SoGapmX1zc4RsB9LHMpd3dNDCf7H6SXCfeZk9rJ8a7424FZn4ej","stackHeight":2}]}],"logMessages":["Program ComputeBudget111111111111111111111111111111 invoke [1]","Program ComputeBudget111111111111111111111111111111 success","Program ComputeBudget111111111111111111111111111111 invoke [1]","Program ComputeBudget111111111111111111111111111111 success","Program ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL invoke [1]","Program log: Create","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]","Program log: Instruction: GetAccountDataSize","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 1569 of 244333 compute units","Program return: TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA pQAAAAAAAAA=","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success","Program 11111111111111111111111111111111 invoke [2]","Program 11111111111111111111111111111111 success","Program log: Initialize the associated token account","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]","Program log: Instruction: InitializeImmutableOwner","Program log: Please upgrade to SPL Token 2022 for immutable owner support","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 1405 of 237746 compute units","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]","Program log: Instruction: InitializeAccount3","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4188 of 233864 compute units","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success","Program ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL consumed 20307 of 249700 compute units","Program ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL success","Program 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P invoke [1]","Program log: Instruction: Buy","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA invoke [2]","Program log: Instruction: Transfer","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA consumed 4645 of 210756 compute units","Program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA success","Program 11111111111111111111111111111111 invoke [2]","Program 11111111111111111111111111111111 success","Program 11111111111111111111111111111111 invoke [2]","Program 11111111111111111111111111111111 success","Program 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P invoke [2]","Program 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P consumed 2003 of 198668 compute units","Program 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P success","Program data: vdt/007mYe51DCMfJMDc1xzkzw+3T0/IL5MwvSeD8fHKYZ6ghuF0H51FBAAAAAAAAOQLVAIAAAAB7/l/o1AL9GidA3MroA1YLKkYNdzsyX8T6twPEOxQ29Jz1UFnAAAAADmDWP0GAAAAW+u01zrPAwA51zQBAAAAAFtTooup0AIA","Program 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P consumed 34453 of 229393 compute units","Program 6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P success"],"preTokenBalances":[{"accountIndex":4,"mint":"8suSDnKVFRyAsTpZ7e2J2seofy6fVhL3cerTfyYppump","uiTokenAmount":{"uiAmount":999286564.142939,"decimals":6,"amount":"999286564142939","uiAmountString":"999286564.142939"},"owner":"TEf2o4WuA8RjzGK5SoE6kPLQzQE4gjrgp4tvErURicA","programId":"TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"}],"postTokenBalances":[{"accountIndex":1,"mint":"8suSDnKVFRyAsTpZ7e2J2seofy6fVhL3cerTfyYppump","uiTokenAmount":{"uiAmount":10000.0,"decimals":6,"amount":"10000000000","uiAmountString":"10000"},"owner":"H9m6fFpfGupwiJAY2aKd9d2MQe1StYSwxRNPcx2NHQuX","programId":"TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"},{"accountIndex":4,"mint":"8suSDnKVFRyAsTpZ7e2J2seofy6fVhL3cerTfyYppump","uiTokenAmount":{"uiAmount":999276564.142939,"decimals":6,"amount":"999276564142939","uiAmountString":"999276564.142939"},"owner":"TEf2o4WuA8RjzGK5SoE6kPLQzQE4gjrgp4tvErURicA","programId":"TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"}],"rewards":[],"loadedAddresses":{"writable":[],"readonly":[]},"computeUnitsConsumed":55060},"version":0,"blockTime":1732367731},"id":0}
"""
    data = parse_transaction(content)
    print(json.dumps(data))
