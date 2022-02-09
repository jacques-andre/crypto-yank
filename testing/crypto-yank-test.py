# Should be running crypto-yank in background
import pyperclip
import json
import time
from termcolor import cprint


# These are random addresses
test_addresses = {
    "btc": "32xtoaovc2qGapAW7gFncnnWRCXTpKCE2D",
    "xmr": "48jewbtxe4jU3MnzJFjTs3gVFWh2nRrAMWdUuUd7Ubo375LL4SjLTnMRKBrXburvEh38QSNLrJy3EateykVCypnm6gcT9bh",
    "eth": "0x33Ddd548FE3a082d753E5fE721a26E1Ab43e3598",
    "dash": "XnfQdQKgXqSLzCp7Q3ZBDfUqeXiS6zxGiM",
    "xrp": "rJumr5e1HwiuV543H7bqixhtFreChWTaHH",
    "doge": "DEZKiDGqGJurNgBCzRsyi85vxccdxZyhD2",
    "tron": "TUpHuDkiCCmwaTZBHZvQdwWzGNm5t8J2b9",
}

with open("../core/addresses.json") as f:
    root_addresses = json.load(f)


def copy_test(root_addresses: dict, test_addresses: dict):
    for key, value in test_addresses.items():
        print(f"Testing:{key}")
        pyperclip.copy(value)
        time.sleep(2)
        if str(pyperclip.paste()) == root_addresses[key]:
            cprint(f"Passed:{key}", "green")
        else:
            cprint(f"Failed:{key}", "red")


copy_test(root_addresses, test_addresses)
