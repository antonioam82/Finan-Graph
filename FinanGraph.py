#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import pandas_datareader as pdr
from datetime import datetime, timedelta
from math import *

fecha_partida = datetime.now() - timedelta(days = 30)

ventana = tkinter.Tk()
ventana.wm_title("Evolucion mensual, Precio acciones")
espacio=ventana.geometry("1000x700")

fig = Figure()

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

datos=fig.add_subplot(111)
datos.plot(grid=True)
plt.show()

button = tkinter.Button(master=ventana, text="SET", bg="gray69")
button.pack(side=tkinter.BOTTOM)
et = tkinter.Entry(master=ventana,width=60)
et.config(bg="gray87", justify="left")
et.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
