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

print("Current Cryptos: ")
for k in addresses.keys():
    print('* ' + k)

print()
for k in addresses.keys():
    print(f"Please enter a address for: {k} (type 0 to not monitor)")
    user_input = str(input(""))
    if k == "legacy_btc" and user_input == "0":
        print("Btc addresses must be monitored!")
        sys.exit()
    if k == "segwit_btc" and user_input == "0":
        print("Btc addresses must be monitored!")
        sys.exit()
    if user_input == "0":
        addresses[k] = 'NULL'
    else:
        addresses[k] = user_input

with open('addresses.json', 'w') as fp:
    json.dump(addresses, fp, indent=4)

print(f"Done! generated addresses.json")
