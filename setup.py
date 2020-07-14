import json
import time
import os
import sys

addresses = {
    "legacy_btc": "",
    "segwit_btc": "",
    "xmr": "",
    "eth": "",
    "lite": "",
    "dash": "",
    "ripple": "",
    "doge": ""
}

print(r""" ___ _ __ _   _ _ __ | |_ ___        _   _  __ _ _ __ | | __
  / __| '__| | | | '_ \| __/ _ \ _____| | | |/ _` | '_ \| |/ /
 | (__| |  | |_| | |_) | || (_) |_____| |_| | (_| | | | |   <
  \___|_|   \__, | .__/ \__\___/       \__, |\__,_|_| |_|_|\_\
            |___/|_|                   |___/
""")


print("created by: github.com/jacques-andre")
print()
time.sleep(1)

if os.path.exists("addresses.json"):
    print("You already have created addresses.json!!")
    sys.exit()

for k, v in addresses.items():
    print(f"Please enter a address for: {k}")
    addresses[k] = input("")

with open('addresses.json', 'w') as fp:
    json.dump(addresses, fp)

print(f"Done! generated addresses.json")
