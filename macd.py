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
        

if __name__ == "__main__":
    main()
    
    
    
