import json
import time
from re import X
import requests
import urllib.request
from keep_alive import keep_alive
# defining key/request url

'''Project discotinued due to Error 451 while requesting data from the URL
Error 451: Which is Unavailable due to legal reasons.'''

keep_alive()


def latest_btc():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    return (f"{data['price']}")


def latest_eth():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    return (f"{data['price']}")


def latest_doge():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=DOGEUSDT"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    return (f"{data['price']}")


count = 0
while count < 10:
    for btc in range(0, 1):
        old_btc_rate = latest_btc()
        print(old_btc_rate)
        time.sleep(120)
        new_btc_rate = latest_btc()
        old_btc_rate = int(float(old_btc_rate))
        new_btc_rate = int(float(new_btc_rate))
        print(new_btc_rate)
        if (new_btc_rate - old_btc_rate) >= 50:
            z = new_btc_rate - old_btc_rate
            tele_url = urllib.request.urlopen(
                f'https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=BTC%20increased%20by%20{z}%20dollars;%20new%20rate%20:%20{new_btc_rate}'
            )

            #z = print("BTC price increased by 100 dollars")
        elif (old_btc_rate - new_btc_rate) >= 50:
            z = old_btc_rate - new_btc_rate
            tele_url = urllib.request.urlopen(
                f'https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=BTC%20decreased%20by%20{z}%20dollars;%20new%20rate%20:%20{new_btc_rate}'
            )
            #z = print*("BTC price dropped by 100 dollars")

        else:
            #tele_url = urllib.request.urlopen('https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=BTC%20price%20stable')
            z = print("BTC price stable")

    for eth in range(0, 1):
        old_eth_rate = latest_eth()
        print(old_eth_rate)
        time.sleep(120)
        new_eth_rate = latest_eth()
        old_eth_rate = int(float(old_eth_rate))
        new_eth_rate = int(float(new_eth_rate))
        print(new_eth_rate)
        if (new_eth_rate - old_eth_rate) >= 25:
            z = new_eth_rate - old_eth_rate
            tele_url = urllib.request.urlopen(
                f'https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=ETH%20increased%20by%20{z}%20dollars;%20new%20rate%20:%20{new_eth_rate}'
            )

            #z = print("ETH price increased by 100 dollars")
        elif (old_eth_rate - new_eth_rate) >= 25:
            z = old_eth_rate - new_eth_rate
            tele_url = urllib.request.urlopen(
                f'https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=ETH%20decreased%20by%20{z}%20dollars;%20new%20rate%20:%20{new_eth_rate}'
            )
            #z = print*("ETH price dropped by 100 dollars")

        else:
            #tele_url = urllib.request.urlopen('https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=ETH%20price%20stable')
            z = print("ETH price stable")

    for doge in range(0, 1):
        old_doge_rate = latest_doge()
        print(old_doge_rate)
        time.sleep(120)
        new_doge_rate = latest_doge()
        old_doge_rate = float(old_doge_rate)
        new_doge_rate = float(new_doge_rate)
        print(new_doge_rate)
        if (new_doge_rate - old_doge_rate) >= 0.001:
            z = new_doge_rate - old_doge_rate
            tele_url = urllib.request.urlopen(
                f'https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=DOGE%20increased%20by%20{z}%20dollars;%20new%20rate%20:%20{new_doge_rate}'
            )
        elif (old_doge_rate - new_doge_rate) >= 0.001:
            z = old_doge_rate - new_doge_rate
            tele_url = urllib.request.urlopen(
                f'https://api.telegram.org/bot5723266083:AAHu7eKZUGXEZFf9oG1WRUP19S_FQhN4eGs/sendMessage?chat_id=-797083430&text=DOGE%20decreased%20by%20{z}%20dollars;%20new%20rate%20:%20{new_doge_rate}'
            )
        else:
            z = print("DOGE price stable")
