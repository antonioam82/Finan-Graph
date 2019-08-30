import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
from VALID import ns

#estilos = plt.style.available
#print(estilos)

#style.use('ggplot')

while True:
    co=input("Comp: ")
    comp = pdr.get_data_yahoo(co,start=datetime.datetime(2019,1,1))

    print(comp)

    datos = comp['Adj Close']

    datos.plot(grid=True)
    plt.show()

    conti=ns(input("¿Continuar?: "))
    if conti == "n":
        break
    
