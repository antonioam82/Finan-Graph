#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas_datareader as pdr
import pickle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
import threading
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter.scrolledtext as sct
import matplotlib.animation as animation
from matplotlib import style
import mplfinance as mpf
import numpy as np

style.use('dark_background')

class finance:
    def __init__(self):
        self.root = Tk()
        self.root.title("Finan Graph 5")
        self.root.geometry("1070x800")
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.grid()

        canvas = FigureCanvasTkAgg(self.fig,master=self.root)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

        self.root.mainloop()

if __name__=="__main__":
    finance()
