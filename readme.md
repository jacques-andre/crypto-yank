<h3 align='center'>A crypto currency clipboard stealer.</h3>
<img align='center' src='.github/logo.png'></img>

<img src='.github/demo.gif'></img>

### Features:

* Written in Python 3
* Support For: `Bitcoin (Legacy & Segwit),Etherum,Dash,Doge,Ripple and Monero.`
* Easy setup script.
* Specific crypto replacement.
* Comprised of regex to find and match addresses.

### About:

**crypto-yank** is a clipboard stealer that replaces crypto-currency addresses found in the clipboard with your malicious address. When no address is found crypto-yank remains dormant until it finds a match.

### Usage:

```
git clone https://github.com/jacques-andre/crypto-yank
cd crypto-yank
pip3 install -r requirements.txt 
python3 setup.py 
python3 crypto-yank.py
```
##### Optional arguments for `crypto-yank.py`:

```
--verbose 
--log > (Logs output to a txt file named log.txt)
```

If you don't want to use the setup script you can provide your own `addresses.json` in the following format:

**`addresses.json`**
```json
{
    "legacy_btc": "leg_ad",
    "segwit_btc": "seg_ad",
    "xmr": "xmr_ad",
    "eth": "eth_ad",
    "dash": "dash_ad",
    "ripple": "ripple_ad",
    "doge": "doge_ad"
}
```
You can also provide the value `NULL` to specific cryptos if you wish not to monitor them:
```
{
    "legacy_btc": "leg_ad",
    "segwit_btc": "seg_ad",
    "xmr": "NULL",
    "eth": "eth_ad",
    "dash": "dash_ad",
    "ripple": "ripple_ad",
    "doge": "doge_ad"
}
```
Using the string `NULL` for `xmr` would now ignore any Monero addresses crypto-yank finds.

##### *NOTE: Bitcoin addresses are mandatory including (segwit and legacy).

Once this file is created in the same directory as `crypto-yank.py` you can run `crypto-yank.py` to start monitoring.

### Demo:

### [Video](https://vimeo.com/437961025)

### Requirements:

[requirements.txt](https://github.com/jacques-andre/crypto-yank/blob/master/requirements.txt)

```
pyperclip==1.8.0
```

### Upcoming/Todo:
- [ ] Add more cryptos!
- [x] Logging to text file.
- [x] Better video demo.

### License
[GPLv3](https://github.com/jacques-andre/crypto-yank/blob/master/LICENSE)
<hr>

**Warning**

I am not responsible for any misuse or damage caused by this program. Use this tool at your own risk!

