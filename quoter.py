#!/usr/bin/env python
# -*- coding: utf-8 -*-
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import argparse
from pynput import keyboard
from colorama import init, Fore, Back, Style
import time

#ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')

def quoter(args,ts):
    counter = 0
    while counter <= 3:
        try:
            data, meta_data = ts.get_intraday(symbol=args.ticker,interval=args.interval, outputsize='full')
            ultimo_dato = data['4. close'].iloc[-1]
            last_date = meta_data['3. Last Refreshed']
            time_zone = meta_data['6. Time Zone']
            print(time_zone + ': ' + last_date + ' | ' + 'Ticker: ' + args.ticker + ' | ' + 'Close: ' + str(ultimo_dato))
            #pprint(data)
            counter += 1
            time.sleep(args.calls)
        except Exception as e:
            print(str(e))
            break

def main():
    parser = argparse.ArgumentParser(prog="QUOTER 0.0",description="Show quotes in real time")
    parser.add_argument('-tick', '--ticker', required=True, type=str, help='Ticker name')
    parser.add_argument('-apik', '--api_key', default='YOUR_API_KEY', type=str, help='API Key')
    parser.add_argument('-ca', '--calls', type=int, default=30, help='Calls to the API')
    parser.add_argument('-int', '--interval', type=str,default='1min',
                        choices=['1min', '5min', '15min', '30min', '1hour', '1day'], help='Interval')

    args = parser.parse_args()
    ts = TimeSeries(key=args.api_key, output_format='pandas')
    quoter(args,ts)
    
    print("OK")

if __name__ == '__main__':
    main()

