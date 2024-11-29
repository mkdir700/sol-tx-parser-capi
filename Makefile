.PHONY: all clean

GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
BUILD_DIR=build

all: $(BUILD_DIR)/libsoltxparser.so

clean:
	$(GOCLEAN)
	rm -rf $(BUILD_DIR)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/libsoltxparser.so: $(BUILD_DIR)
	CGO_ENABLED=1 $(GOBUILD) -buildmode=c-shared -o $@ ./capi
	cp $(BUILD_DIR)/libsoltxparser.so python/src/solana_tx_parser/lib/
	cp $(BUILD_DIR)/libsoltxparser.h python/src/solana_tx_parser/lib/


