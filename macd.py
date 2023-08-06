#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import numpy as np
from os import system
from colorama import Fore, Style, init
import argparse

init()

def validate_date(d):
    try:
        return datetime.strptime(d, '%Y-%m-%d')
    except:
        raise argparse.ArgumentTypeError(Fore.RED + Style.BRIGHT + "Bad date format (must be '%Y-%m-%d')" + Fore.RESET +Style.RESET_ALL)

def get_data(s,st,e):
    try:
        df = yf.download(s, start = st, end = e)
        df["EMA12"] = df.Close.ewm(span=12).mean()
        df["EMA26"] = df.Close.ewm(span=26).mean()
        df["MACD"] = df.EMA12-df.EMA26
        df["Senal"] = df.MACD.ewm(span = 9).mean()
        print(Fore.GREEN)
        print(df)
        print(Fore.RESET)

        plt.subplot(2,1,2)
        plt.plot(df.Senal, color="red")
        plt.plot(df.MACD)
        Buy, Sell = [], []
        
        plt.subplot(2,1,2)
        plt.plot(df.Senal, color="red")
        plt.plot(df.MACD)
        Buy, Sell = [], []
        for i in range(2, len(df)):
            if df.MACD.iloc[i] > df.Senal.iloc[i] and df.MACD.iloc[i-1] < df.Senal.iloc[i-1]:
                Buy.append(i)
            elif df.MACD.iloc[i] < df.Senal.iloc[i] and df.MACD.iloc[i-1] > df.Senal.iloc[i-1]:
                Sell.append(i)

        print("Dates sales:")
        print(df.iloc[Sell].index, df.iloc[Sell].Close)
        sellinfo = df.iloc[Sell].index, df.iloc[Sell].Close
        print("Bullish dates:")
        print(df.iloc[Buy].index, df.iloc[Buy].Close)
        buyinfo = df.iloc[Buy].index, df.iloc[Buy].Close

        #Get data from bullish
        df1 = pd.DataFrame.from_records(buyinfo)
        print(df1)
        #Dataframe to dict:
        diccionario = df1.to_dict()
        #counting the data for get the last date for buy:
        keys = list(diccionario.keys())
        contarkeys = keys[-1]
        print("count:",contarkeys)
        print("Last info for buy:")
        print(diccionario[contarkeys])
        print("Last date for buy:")
        date1 = diccionario[contarkeys][0]
        dateforbuy = date1.strftime("%d/%m/%Y")
        print(dateforbuy)
        print("########")
        print("Today date:")
        now = datetime.now()
        datetoday = now.strftime("%d/%m/%Y")
        print(datetoday)
        print("Yesterday date:")
        yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
        print(yesterday)

        print("Final decision:")
        if str(dateforbuy) == str(yesterday):
            print("MACD = BUY")
        else:
            print("Not news")


        
        
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + str(e) + Fore.RESET +Style.RESET_ALL )

def main():
    parser = argparse.ArgumentParser(prog="macd 0.0", description="MCAD from CMD",
                                     epilog="")
    parser.add_argument('-sym','--symbol',required=True,type=str, help="Thicker symbol")
    parser.add_argument('-st','--start',type=validate_date, required=True, help="Start date")
    parser.add_argument('-e','--end',type=validate_date, required=True, help="End date")

    args = parser.parse_args()
    print(args.start)
    if str(args.start) >= str(args.end):
        parser.error(Fore.RED + Style.BRIGHT + "Start date must be minor than end date" + Fore.RESET +Style.RESET_ALL)

    get_data(args.symbol,args.start,args.end)
        

if __name__ == "__main__":
    main()
    
