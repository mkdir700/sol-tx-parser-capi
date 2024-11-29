.PHONY: all clean

GOCMD=go
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
BUILD_DIR=build

# 检测操作系统
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
    OUTPUT=libsoltxparser.dylib
else ifeq ($(UNAME_S),Linux)
    OUTPUT=libsoltxparser.so
else ifeq ($(OS),Windows_NT)
    OUTPUT=soltxparser.dll
else
    $(error Unsupported operating system)
endif

all: $(BUILD_DIR)/$(OUTPUT)

clean:
	$(GOCLEAN)
	rm -rf $(BUILD_DIR)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/$(OUTPUT): $(BUILD_DIR)
	CGO_ENABLED=1 $(GOBUILD) -buildmode=c-shared -o $@ ./capi
	cp $(BUILD_DIR)/$(OUTPUT) python/src/solana_tx_parser/lib/
	cp $(BUILD_DIR)/*.h python/src/solana_tx_parser/lib/


