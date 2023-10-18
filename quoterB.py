#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
import argparse
import yfinance as yf
from pynput import keyboard
from colorama import init, Fore, Back, Style
import time

init()

stop = False

def on_press(key):
    global stop
    if key == keyboard.Key.space:
        stop = True
        print('Wait until application ends...')
        return False

def quoter(args):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    try:
        while stop == False:
            #print("HELLO")
            stock_data = yf.download(args.ticker, period="1d",interval="1m")
            
            last_close_price = stock_data["Close"].iloc[-1]
            last_volume = stock_data["Volume"].iloc[-1]
            last_open_price = stock_data["Open"].iloc[-1]
            last_adj_close = stock_data["Adj Close"].iloc[-1]
            last_high_price = stock_data["High"].iloc[-1]
            last_low_price = stock_data["Low"].iloc[-1]
            current_datetime = stock_data.index[-1]
            
            print(Fore.GREEN + Style.BRIGHT + f"{current_datetime} | Ticker: {args.ticker} | Low: {last_low_price:.2f} | High: {last_high_price:.2f} | Open: {last_open_price:.2f} |"
                  f" Volume: {last_volume:.2f} | Close: {last_close_price:.2f}" + Fore.RESET + Style.RESET_ALL)

            time.sleep(args.time_delay)

            if stop == True:
                print("\nProcess interrupted by user.")
                break
                
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + str(e) + Fore.RESET + Style.RESET_ALL)

def main():
    parser = argparse.ArgumentParser(prog="QUOTER 0.0",description="Show quotes in real time")
    parser.add_argument('-tick', '--ticker', required=True, type=str, help='Ticker name')
    parser.add_argument('-delay', '--time_delay', type=float, default=30, help='Call delay to the API, in seconds')

    args = parser.parse_args()
    #ts = "hhd"
    quoter(args)

if __name__ == '__main__':
    main()
