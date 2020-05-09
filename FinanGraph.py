import pandas_datareader as pdr
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

"""def get_info():
    init_date = datetime.now() - timedelta(days = int(entry3.get()))
    info = pdr.get_data_yahoo(entry.get(),start = init_date)"""

ventana = Tk()
ventana.title("Finan Graph")
ventana.geometry("1040x700")
ventana.configure(background="light blue")
symbol_entry = StringVar()

fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

labelSym = Label(master=ventana,bg="light blue",text="Symbol:",width=8)
labelSym.pack(side=LEFT)
entry = Entry(master=ventana,width=8)
entry.pack(side=LEFT)
labelCom = Label(master=ventana,bg="light blue",text="Compare with:",width=10)
labelCom.place(x=153,y=0)
entry2 = Entry(master=ventana,width=8)
entry2.place(x=240,y=1)
labelRange = Label(master=ventana,text="Periodo en días",width=13)
labelRange.place(x=270,y=0)

plt.show()

ventana.mainloop()

