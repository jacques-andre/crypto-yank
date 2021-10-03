import pprint
import time
from termcolor import cprint
import os
import json
import pyperclip

with open("words.txt") as words_file:
    words = words_file.read().splitlines()

with open("addresses_test.json") as addresses_test:
    addresses = json.load(addresses_test)


def main():
    w_count = 0
    a_count = 0
    for word in words:
        print(f"word: {word}")
        pyperclip.copy(word)
        time.sleep(2)
        word_in = pyperclip.paste()

        if word == word_in:
            cprint("Passed!", "green")
            w_count += 1
        else:
            cprint("Failed!", "red")
            print(f"word: {word}, word_in: {word_in}")

    for k, v in addresses.items():
        print(f"address: {k}")
        pyperclip.copy(k)
        time.sleep(2)
        paste = pyperclip.paste()

        if paste == v:
            cprint("Passed!", "green")
            a_count += 1
        else:
            cprint("Failed!", "red")
            print(f"ad: {k}, expected: {v}")

    print(f"Word count: {w_count}, len: {len(words)}, %: {w_count / len(words)}")
    print(f"ad count: {a_count}, len: {len(addresses)}, %: {a_count / len(addresses)}")


main()
