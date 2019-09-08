import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime, timedelta
from VALID import ns, OKI

#estilos = plt.style.available
#print(estilos)

style.use('dark_background')

while True:
    co=input("Comp: ")
    param=input("Param: ")
    period=OKI(input("Periodo en días: "))

    fecha_partida = datetime.now() - timedelta(days = period)
    
    try:
        comp = pdr.get_data_yahoo(co,start= fecha_partida)
        print(comp)

        datos = comp[param]
        datos.plot(grid=True,figsize=(13,7))
        plt.title("Datos "+co)
        plt.show()
    except:
        print("HUBO UN PROBLEMA AL ESTABLECER LA CONEXION")

    conti=ns(input("¿Continuar?: "))
    if conti == "n":
        break
    
