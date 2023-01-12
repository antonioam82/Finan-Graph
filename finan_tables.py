import argparse
import sys
import yfinance as yf
from datetime import datetime
import plotext as plt
#from colorama import init, Fore, Back

#init()

now = datetime.now()
day = now.day
month = now.month
year = now.year

def main():
    
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--head',default=0,type=int,help='Número de lineas iniciales')
    group.add_argument('--tail',default=0,type=int,help='Número de lineas finales')
    parser.add_argument('--symbol',type=str,help="Introduce ticker/s.")
    parser.add_argument('--start',type=str,help="Fecha inicial de la serie")
    parser.add_argument('--end',default='{}/{}/{}'.format(year,month,day),type=str,help="Fecha final de la serie")
    parser.add_argument('--interval',default='d',choices=['d','wk','mo','m','w'],type=str,help="Intervalos de tiempo")
    #parser.add_argument('-plot',default=False,type=bool,help="Grafica")

    args=parser.parse_args()
    show_table(args)

def show_table(args):
    print("RETRIEVING DATA...")
    symbol = yf.Ticker(args.symbol)
    df = symbol.history(start=args.start,end=args.end, interval='1m')#nterval=args.interval)
    
    #print(""+Back.BLUE+Fore.WHITE)
    print("")
    if args.tail > 0:
        print(df.tail(args.tail))
    elif args.head > 0:
        print(df.head(args.head))
    else:
        print(df)
    #print(Back.RESET+Fore.RESET)
    
if __name__=='__main__':
    main()

