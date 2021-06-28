#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas_datareader import data as pdr
#import pickle
from tkinter import *
#from tkinter import ttk
#from tkinter import messagebox
import datetime as date
#import threading
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#import tkinter.scrolledtext as sct
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('dark_background')
root = Tk()
root.title("Finan Graph 5")
root.geometry("1160x800")
actv = True
fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

def MA(df, n):
    MA = pd.Series(pd.Series.rolling(df['Close'],n).mean(),name='MA_'+str(n))
    df = df.join(MA)
    return df

def EMA(df, n):
    EMA = pd.Series(pd.Series.ewm(df['Close'],span = n, min_periods = n-1, adjust=False).mean(), name='EMA_'+str(n))
    df = df.join(EMA)
    return df

def make_graph():
    enddate = date.datetime(2019,11,1)
    startdate = date.datetime(2010,1,1)
    tick = 'IBM'
    ipc = pdr.get_data_yahoo(tick, start = startdate, end = enddate)
    df = EMA(ipc, 50)
    df2 = MA(df, 50)
    df2 = df2[['Close','MA_50','EMA_50']]

    ax1.plot(df2)

def represent(i):
    global actv
    if actv == True:
        print("activo")

ani = animation.FuncAnimation(fig, represent, interval=1000)

make_graph()

root.mainloop()
