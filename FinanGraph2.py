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

class finance:
    def __init__(self):
        self.root = Tk()
        self.root.title("Finan Graph 5")
        self.root.geometry("1160x800")
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.grid()

        canvas = FigureCanvasTkAgg(self.fig,master=self.root)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

        self.make_graph()

        self.root.mainloop()

    def MA(self, df, n):
        MA = pd.Series(pd.Series.rolling(df['Close'],n).mean(),name='MA_'+str(n))
        df = df.join(MA)
        return df

    def EMA(self, df, n):
        EMA = pd.Series(pd.Series.ewm(df['Close'],span = n, min_periods = n-1, adjust=False).mean(), name='EMA_'+str(n))
        df = df.join(EMA)
        return df

    def make_graph(self):
        enddate = date.datetime(2019,11,1)
        startdate = date.datetime(2010,1,1)
        tick = 'IBM'
        ipc = pdr.get_data_yahoo(tick, start = startdate, end = enddate)
        df = self.EMA(ipc, 50)
        df2 = self.MA(df, 50)
        df2 = df2[['Close','MA_50','EMA_50']]

        #df2.plot(figsize = (8,8))#16,8
        self.ax1.plot(df2)
        

if __name__=="__main__":
    finance()
