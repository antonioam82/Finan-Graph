import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime, timedelta
from VALID import ns, OKI

#estilos = plt.style.available
#print(estilos)

style.use('dark_background')

tipos_datos = ["High","Low","Volume","Adj Close"]

comps={"NETFLIX":"NFLX","GOOGLE":"GOGL","APPLE":"AAPL","GENERAL MOTORS":"GM","SILVER":"F",
      "AMAZON":"AMZN","BANKIA":"BNK","ORO":"GOLD","FANUC":"FANUY","BITCOIN":"BTC-EUR","TESLA":"TSLA",
       "IBEX":"^IBEX","NASDAQ":"^IXIC"}

def enum(opcions):
    for i,opcion in enumerate(opcions):
        print(i,opcion)
    eleccion = OKI(input("Introduzca número correspondiente a su opción: "))
    while eleccion > (len(opcions)-1):
        eleccion = OKI(input("Introduzca indice válido correspondiente a su opción: "))
    assert eleccion in range(len(opcions))
    tex_elec = opcions[eleccion]
    return tex_elec


while True:
    compa=(input("Comp: ")).upper()
    print("\n****TIPO DE DATO****")
    param=enum(tipos_datos)
    period=OKI(input("Periodo en días: "))
    co=compa
    if co in comps:
        co=comps[co]
    fecha_partida = datetime.now() - timedelta(days = period)

    
    try:
        comp = pdr.get_data_yahoo(co,start= fecha_partida)
        print(comp)
        
        diferencia=float(comp[param][-1]-comp[param][-2])

        datos = comp[param]
        datos.plot(grid=True,figsize=(13,7))
        plt.title("Datos: "+compa+" "+"("+str(round(diferencia,2))+")")
        plt.show()
    except:
        print("HUBO UN PROBLEMA AL GENERAR LA GRÁFICA")

    conti=ns(input("¿Continuar?: "))
    if conti == "n":
        break
    
