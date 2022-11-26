import argparse
import sys
import pandas_datareader as pdr
from datetime import datetime
#from colorama import init, Fore, Back

#init()

now = datetime.now()
day = now.day
month = now.month
year = now.year

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-symbol',type=str,help="Introduce simbolo")
    parser.add_argument('-start',type=str,help="Fecha inicial de la serie")
    parser.add_argument('-end',default='{}/{}/{}'.format(year,month,day),type=str,help="Fecha final de la serie")
    parser.add_argument('-interval',default='d',type=str,help="Intervalos de tiempo")
    #parser.add_argument('-tail',default=0,type=int,help="Valores finales")
    #parser.add_argument('-head',default=0,type=int,help="Valores iniciales")
    args=parser.parse_args()
    show_table(args)
    

def show_table(args):
    print("RETRIEVING DATA...")
    fecha1 = args.start
    fecha_dt1 = fecha1.split("/")
    fecha2 = args.end
    fecha_dt2 = fecha2.split("/")
    symbols = args.symbol
    symbols_data = symbols.split(",")
    
    df = pdr.get_data_yahoo(symbols_data,start=datetime(int(fecha_dt1[0]),int(fecha_dt1[1]),int(fecha_dt1[2])),
                            end=datetime(int(fecha_dt2[0]),int(fecha_dt2[1]),int(fecha_dt2[2])),interval=args.interval)
    
    #print(""+Back.BLUE+Fore.WHITE)
    print("")
    print(df)
    #print(Back.RESET+Fore.RESET)

if __name__=='__main__':
    main()
