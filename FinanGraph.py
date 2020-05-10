import pandas_datareader as pdr
from tkinter import *
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as animation
import numpy as np


ventana = Tk()
ventana.title("Finan Graph")
ventana.geometry("1040x700")
ventana.configure(background="light blue")
symbol_entry = StringVar()
time_range = IntVar()
actv = False
info = ""

fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()


canvas = FigureCanvasTkAgg(fig,master=ventana)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, ventana)
toolbar.update()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

def activate():
    global actv
    actv = True

def get_info():
    global actv
    ax1.clear()
    ax1.grid()
    init_date = datetime.now() - timedelta(days = int(entry3.get()))
    info = pdr.get_data_yahoo(entry.get(),start = init_date)
    ax1.plot(info)
    actv = False

def represent(i):
    global actv
    if actv == True:
        get_info()
    #ani.event_source.start()

ani = animation.FuncAnimation(fig, represent, interval=1000)  

labelSym = Label(master=ventana,bg="light blue",text="Symbol:",width=8,height=2)
labelSym.pack(side=LEFT)
entry = Entry(master=ventana,width=8)
entry.pack(side=LEFT)
labelCom = Label(master=ventana,bg="light blue",text="Compare with:",width=10,height=2)
labelCom.place(x=125,y=0)
entry2 = Entry(master=ventana,width=8)
entry2.place(x=210,y=8)
labelRange = Label(master=ventana,text="Periodo en días:",bg="light blue",width=13,height=2)
labelRange.place(x=272,y=0)
entry3 = Entry(master=ventana,width=8,textvariable=time_range)
entry3.place(x=369,y=8)
graph = Button(master=ventana,text="VIEW GRAPH",command=activate,height=1)
graph.place(x=958,y=6)

plt.show()

ventana.mainloop()

