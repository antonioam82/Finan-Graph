#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys ####################
import yfinance as yf
import pathlib
from datetime import datetime
from colorama import Fore, init
import matplotlib.pyplot as plt

init()

now = datetime.now()
day = now.day
month = now.month
year = now.year
head = ""
actions = False
tickers = []
indexed_syms = ['IXIC','N225','GSPC','GDAXI','FCHI','DJI','IBEX','DJT','STOXX50E','FTSE','BFX','AEX',
                'HSI','BVSP','MXX','ATX','SSMI','OMXC20','OSEAX','OMXSPI','JKSE','NSEMDCP50','N100','NDX',
                'CRSMID','KS11','TWII','TA125.TA','KLSE','NZ50','CASE30','BVSP','IPSA','JN0U.JO','STI']

def main():
    global actions
    parser = argparse.ArgumentParser(prog="f-tables",conflict_handler='resolve',description="Display finantial tables on your terminal.",
                                     epilog= "REPO: https://github.com/antonioam82/f-tables")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-hd','--head',default=0,type=int,help='Number of head lines')
    group.add_argument('-tl','--tail',default=0,type=int,help='Number of end lines')
    parser.add_argument('-sym','--symbol',required=True,type=str,help="Ticker symbol")
    parser.add_argument('-i','--info',type=str,default="All",choices=["All","Open","High","Low","Close","Volume","Dividends","Stock_Splits"],help="Quote data")
    parser.add_argument('-s','--start',type=str,default=None,help="Start date of time series")
    parser.add_argument('-act','--actions',default=None,action='store_true',help="Show actions")
    parser.add_argument('-e','--end',default='{}-{}-{}'.format(year,month,day),type=str,help="End date of time series")
    parser.add_argument('-int','--interval',default='1d',
                        choices=["1m","2m","5m","15m","30m","60m","90m","1h","1d","5d","1wk","1mo","3mo"],type=str,help="Time intervals")
    parser.add_argument('--plot','-plt',default=None,action='store_true',help="Show graph")
    parser.add_argument('--save','-sv',type=str,default=None,help="Save table")

    args=parser.parse_args()
    if args.actions:
        actions = True
        
    show_table(args)

def save_table(args,df):
    doc = args.save
    extension = pathlib.Path(doc).suffix
    if extension == ".txt" or extension == ".xlsx":
        try:
            if extension == ".txt":
                with open(doc, "w") as document:
                    document.write(head+"\n\n"+str(df))
            else:
                df.to_excel(doc,index=False)
            print(Fore.YELLOW+f"\nDocument saved as '{doc}'"+Fore.RESET)
            
        except Exception as e:
            print(Fore.RED+f"\nUNEXPECTED ERROR: {str(e)}"+Fore.RESET)
            
    else:
        print(Fore.RED+"\nBAD FILE FORMAT: File extension must be '.txt' or '.xlsx'"+Fore.RESET)

def head(args):
    global head
    if args.start:
        head = f"SYMBOL: ({args.symbol}), PERIOD: {args.start}/{args.end}, INTERVAL: {args.interval}, QUOTE: {args.info}\n"
        print("\n"+Fore.GREEN+head)
    else:
        head = f"SYMBOL: ({args.symbol}), PERIOD: Max, INTERVAL: {args.interval}, QUOTE: {args.info}\n"
        print("\n"+Fore.GREEN+head)

def plot_graph(args,df):
    plt.title(f'{args.symbol}-{args.info}')
    plt.plot(df)
    plt.xlabel("TIME")
    plt.ylabel("PRICE")
    plt.legend(loc='best',facecolor="w")
    plt.xticks(rotation=20)
    plt.grid()
    plt.legend(tickers,loc='best', shadow=False)
    plt.show()

    
def show_table(args):
    global tickers
    try:
        print("RETRIEVING DATA...")
        if args.symbol.count(',') >= 1:
            lista = args.symbol.replace(',',' ').split(" ")
            c=0
            for i in lista:
                if i in indexed_syms:
                    lista[c] = "^"+i
                c+=1
            symbols = (" ").join(tuple(lista))
            symbol = yf.Tickers(symbols)
            tickers = lista
            tickers.sort()
        else:
            if args.symbol in indexed_syms:
                symbol = yf.Ticker("^"+args.symbol)
            else:
                symbol = yf.Ticker(args.symbol)
            tickers = [args.symbol]
        
        if args.info == "All":
            if args.start:
                df = symbol.history(start=args.start,end=args.end, interval=args.interval, actions = actions)
            else:
                df = symbol.history(period="max",end=args.end, interval=args.interval, actions = actions)
        else:
            if args.start is not None:
                df = symbol.history(start=args.start,end=args.end, interval=args.interval)[args.info.replace('_',' ')]
            else:
                df = symbol.history(period="max",end=args.end, interval=args.interval)[args.info.replace('_',' ')]

        if df.empty == False:
            if args.tail > 0:
                df = df.tail(args.tail)
            elif args.head > 0:
                df = df.head(args.head)
            head(args)
            print(df)

            if args.save is not None:
                save_table(args,df)        
            
            if args.plot:
                if args.info != "All":
                    plot_graph(args,df)
                else:
                    args.info = 'Close'
                    plot_graph(args,df['Close'])
        else:
            print(Fore.RED+"\nEmpty dataframe")
            

        print(Fore.RESET)
    except Exception as e:
        print(Fore.RED+f"\nUNEXPECTED ERROR: {str(e)}"+Fore.RESET)
    
if __name__=='__main__':
    main()
