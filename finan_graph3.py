#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas_datareader as pdr
from alpha_vantage.techindicators import TechIndicators
import pickle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter.scrolledtext as sct
import matplotlib.animation as animation
from matplotlib import style
import mplfinance as mpf
import numpy as np

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Finan Graph")
        self.ventana.geometry("1070x800")
        self.ventana.configure(background="light blue")

        style.use('seaborn-notebook')
        
        fig = Figure()
        fig.add_subplot(111)
        init_date = datetime.now() - timedelta(days = 100)
        info = pdr.get_data_yahoo('GOOGL',start = init_date)
        print(info)
        fig, ax = mpf.plot(
            data=info,
            type='candle',
            #style='charles',
            title="GOOGLE",
            ylabel='Price ($)',
            volume=False,
            #ylabel_lower='Shares\nTraded',
            show_nontrading=False,
            returnfig = True
            )
        

        canvas = FigureCanvasTkAgg(fig,master=self.ventana)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, self.ventana)
        toolbar.update()
        canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

        self.ventana.mainloop()

if __name__=="__main__":
    App()
