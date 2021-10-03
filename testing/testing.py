import time
from termcolor import cprint
import json
import pyperclip

# open testing files
with open("words.txt") as words_file:
    WORDS = words_file.read().splitlines()

with open("addresses_test.json") as addresses_test:
    ADDRESSES = json.load(addresses_test)


def word_test() -> list:
    # copies a word to the clipboard and tests when pasting if it is the same word
    failed = []
    for word in WORDS:
        print(f"Testing: {word}")
        pyperclip.copy(word)
        time.sleep(1)  # small delay, ensures crypto-yank reads in clipboard
        pasted = pyperclip.paste()

        if pasted == word:
            cprint("Passed!", "green")
        else:
            cprint("Failed!", "red")
            failed.append(word)
            break
    return failed


def address_test() -> list:
    failed = []
    for k, v in ADDRESSES.items():
        print(f"Testing: {k}")
        pyperclip.copy(k)
        time.sleep(1)  # small delay, ensures crypto-yank reads in clipboard
        pasted = pyperclip.paste()

        if pasted == v:
            cprint("Passed!", "green")
        else:
            cprint("Failed!", "red")
            failed.append(k)
            break
    return failed


def main():
    print(f"Running tests... Make sure crypto-yank.py is running!")
    failed_words = word_test()
    failed_ad = address_test()


main()
