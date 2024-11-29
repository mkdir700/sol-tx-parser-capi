package main

/*
#include <stdlib.h>
#include <stdint.h>

typedef struct {
    char* error;
    char* result;
} ParseResult;
*/
import "C"
import (
	"encoding/json"
	"unsafe"

	"github.com/0xjeffro/tx-parser/solana"
	"github.com/0xjeffro/tx-parser/solana/types"
)

func _parseTransaction(txData string) (string, error) {
	var result types.RPCResponse

	err := json.Unmarshal([]byte(txData), &result)
	if err != nil {
		return "", err
	}

	var txs []types.RawTx
	txs = append(txs, result.Result)
	b, err := json.Marshal(txs)

	if err != nil {
		return "", err
	}

	parsed, err := solana.Parser(b)

	if err != nil {
		return "", err
	}

	parsedJson, err := json.Marshal(parsed)

	if err != nil {
		return "", err
	}

	return string(parsedJson), nil
}

//export ParseTransaction
func ParseTransaction(txData *C.char) C.ParseResult {
	parsedJson, err := _parseTransaction(C.GoString(txData))
	if err != nil {
		return C.ParseResult{
			error:  C.CString(err.Error()),
			result: nil,
		}
	}
	return C.ParseResult{
		error:  nil,
		result: C.CString(parsedJson),
	}
}

//export FreeParseResult
func FreeParseResult(result C.ParseResult) {
	if result.error != nil {
		C.free(unsafe.Pointer(result.error))
	}
	if result.result != nil {
		C.free(unsafe.Pointer(result.result))
	}
}
