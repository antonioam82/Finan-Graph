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

ventana = tkinter.Tk()
ventana.wm_title("Evolucion mensual, Precio acciones")
espacio=ventana.geometry("1000x700")

fig = Figure()

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)





tkinter.mainloop()
