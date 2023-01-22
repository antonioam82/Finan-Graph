import argparse
import sys
import yfinance as yf
from datetime import datetime
#import plotext as plt
from colorama import Fore, init

init()

now = datetime.now()
day = now.day
month = now.month
year = now.year

def main():
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-hd','--head',default=0,type=int,help='Número de lineas iniciales')
    group.add_argument('-tl','--tail',default=0,type=int,help='Número de lineas finales')
    parser.add_argument('-sym','--symbol',required=True,type=str,help="Introduce ticker/s.")
    parser.add_argument('-i','--info',type=str,default="All",choices=["All","Open","High","Low","Close","Volume","Dividends","Stock_Splits"],help="Data")
    parser.add_argument('-s','--start',type=str,default=None,help="Fecha inicial de la serie")
    parser.add_argument('-e','--end',default='{}-{}-{}'.format(year,month,day),type=str,help="Fecha final de la serie")
    parser.add_argument('-int','--interval',default='1d',
                        choices=["1m","2m","5m","15m","30m","60m","90m","1h","1d","5d","1wk","1mo","3mo"],type=str,help="Intervalos de tiempo")
    #parser.add_argument('--plot','-plt',default=False,type=bool,help="Grafica")

    args=parser.parse_args()
    show_table(args)

def show_table(args):
    try:
        print("RETRIEVING DATA...")
        symbol = yf.Ticker(args.symbol)
        print("\n"+Fore.GREEN+f"SYMBOL: {args.symbol}")
        if args.info == "All":
            if args.start is not None:
                df = symbol.history(start=args.start,end=args.end, interval=args.interval)
            else:
                df = symbol.history(period="max",end=args.end, interval=args.interval)
        else:
            if args.start is not None:
                df = symbol.history(start=args.start,end=args.end, interval=args.interval)[args.info.replace('_',' ')]
            else:
                df = symbol.history(period="max",end=args.end, interval=args.interval)[args.info.replace('_',' ')]

        if args.tail > 0:
            print(df.tail(args.tail))
        elif args.head > 0:
            print(df.head(args.head))
        else:
            print(df)
        print(Fore.RESET)
    except Exception as e:
        print(Fore.RED+f"UNEXPECTED ERROR: {str(e)}"+Fore.RESET)
    
if __name__=='__main__':
    main()


