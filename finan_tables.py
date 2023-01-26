#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
import yfinance as yf
from datetime import datetime
from colorama import Fore, init
import matplotlib.pyplot as plt

init()

now = datetime.now()
day = now.day
month = now.month
year = now.year

def main():
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-hd','--head',default=0,type=int,help='Number of head lines')
    group.add_argument('-tl','--tail',default=0,type=int,help='Number of end lines')
    parser.add_argument('-sym','--symbol',required=True,type=str,help="Ticker symbol")
    parser.add_argument('-i','--info',type=str,default="All",choices=["All","Open","High","Low","Close","Volume","Dividends","Stock_Splits"],help="Quote data")
    parser.add_argument('-s','--start',type=str,default=None,help="Start date of time series")
    parser.add_argument('-e','--end',default='{}-{}-{}'.format(year,month,day),type=str,help="End date of time series")
    parser.add_argument('-int','--interval',default='1d',
                        choices=["1m","2m","5m","15m","30m","60m","90m","1h","1d","5d","1wk","1mo","3mo"],type=str,help="Time intervals")
    parser.add_argument('--plot','-plt',default=None,action='store_true',help="Show graph")
    parser.add_argument('--save','-sv',action="store_true",help="Save table")

    args=parser.parse_args()
    show_table(args)

def save_table(df):
    doc = "f_table.txt"
    with open(doc, "w") as document:
        document.write(str(df))
    print(Fore.YELLOW+f"\nSaved document as f_table.txt"+Fore.RESET)

def head(args):
    if args.start:
        print("\n"+Fore.GREEN+f"SYMBOL: {args.symbol}, PERIOD: {args.start}/{args.end}, INTERVAL: {args.interval}, QUOTE: {args.info}\n")
    else:
        print("\n"+Fore.GREEN+f"SYMBOL: {args.symbol}, PERIOD: Max, INTERVAL: {args.interval}, QUOTE: {args.info}\n")

def show_table(args):
    try:
        print("RETRIEVING DATA...")
        symbol = yf.Ticker(args.symbol)
        head(args)
        if args.info == "All":
            if args.start:
                df = symbol.history(start=args.start,end=args.end, interval=args.interval)
            else:
                df = symbol.history(period="max",end=args.end, interval=args.interval)

        else:
            if args.start is not None:
                df = symbol.history(start=args.start,end=args.end, interval=args.interval)[args.info.replace('_',' ')]
            else:
                df = symbol.history(period="max",end=args.end, interval=args.interval)[args.info.replace('_',' ')]

        if args.tail > 0:
            df = df.tail(args.tail)
        elif args.head > 0:
            df = df.head(args.head)

        print(df)
            
        if args.plot:
            plt.plot(df)
            plt.grid()
            plt.show()

        if args.save:
            save_table(df)
            
        print(Fore.RESET)
    except Exception as e:
        print(Fore.RED+f"\nUNEXPECTED ERROR: {str(e)}"+Fore.RESET)
    
if __name__=='__main__':
    main()

