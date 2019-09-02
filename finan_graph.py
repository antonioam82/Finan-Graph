import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime, timedelta
from VALID import ns

#estilos = plt.style.available
#print(estilos)

#style.use('ggplot')

fecha_partida = datetime.now() - timedelta(days = 30)

while True:
    co=input("Comp: ")
    
    try:
        comp = pdr.get_data_yahoo(co,start= fecha_partida)
        print(comp)

        datos = comp['Adj Close']
        datos.plot(grid=True)
        plt.show()
    except:
        print("HUBO UN PROBLEMA AL ESTABLECER LA CONEXION")

    conti=ns(input("¿Continuar?: "))
    if conti == "n":
        break
    
    