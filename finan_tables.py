import argparse
import sys
import pandas_datareader as pdr
from datetime import datetime

now = datetime.now()
day = now.day
month = now.month
year = now.year

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-symbol',type=str,help="Introduce simbolo")
    parser.add_argument('-start',type=str,help="Fecha inicial de la serie")
    parser.add_argument('-end',default='{}/{}/{}'.format(year,month,day),type=str,help="Fecha final de la serie")
    #parser.add_argument('-tail',default=0,type=int,help="Valores finales")
    #parser.add_argument('-head',default=0,type=int,help="Valores iniciales")
    args=parser.parse_args()
    show_table(args)
    

def show_table(args):
    fecha1 = args.start
    fecha_dt1 = fecha1.split("/")
    fecha2 = args.end
    fecha_dt2 = fecha2.split("/")
    
    df = pdr.get_data_yahoo(args.symbol,start=datetime(int(fecha_dt1[0]),int(fecha_dt1[1]),int(fecha_dt1[2])),
                                end=datetime(int(fecha_dt2[0]),int(fecha_dt2[1]),int(fecha_dt2[2])))
    print("")
    print(df)

if __name__=='__main__':
    main()
