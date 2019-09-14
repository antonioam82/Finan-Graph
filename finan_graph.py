import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime, timedelta
from VALID import ns, OKI

#estilos = plt.style.available
#print(estilos)

style.use('dark_background')

comps={"GOGL":"GOOGLE","AAPL":"Apple","GM":"General Motors","F":"SILVER",
       "AMZN":"Amazon","BNK":"Bankia","GOLD":"Oro"}

while True:
    co=(input("Comp: ")).upper()
    param=input("Param: ")
    period=OKI(input("Periodo en días: "))

    fecha_partida = datetime.now() - timedelta(days = period)

    
    try:
        comp = pdr.get_data_yahoo(co,start= fecha_partida)
        print(comp)
        
        diferencia=float(comp[param][-1]-comp[param][-2])

        datos = comp[param]
        datos.plot(grid=True,figsize=(13,7))
        if co in comps:
            co = comps[co]
        plt.title("Datos: "+co+" "+"("+str(round(diferencia,2))+")")
        plt.show()
    except:
        print("HUBO UN PROBLEMA AL ESTABLECER LA CONEXION")

    conti=ns(input("¿Continuar?: "))
    if conti == "n":
        break
    
