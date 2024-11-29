#ifndef SOLANA_TX_PARSER_H
#define SOLANA_TX_PARSER_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    char* error;
    char* result;
} ParseResult;

ParseResult ParseTransaction(const char* txData);
void FreeParseResult(ParseResult result);

#ifdef __cplusplus
}
#endif

#endif // SOLANA_TX_PARSER_H
