#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas_datareader import data as pdr
from sklearn.preprocessing import MinMaxScaler
import pickle
import ta
import yfinance as yf

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as sct
import datetime as date
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as animation
from matplotlib import style
import threading
import os
import numpy as np

style.use('dark_background')
root = Tk()
root.title("Finan Graph 3")
root.configure(background="gray")
root.geometry("1160x800")#1160
start_date = StringVar()
end_date = StringVar()
df2 = ""
table_head = ""
actv = False
fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()
selected_items = ["Close"]
item_list = ["Low","High","Open","Close","MA_50","MA_200"]

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)


tick_entry = ttk.Combobox(root,width=10)
#tick_entry["values"]=used_symbols
tick_entry.place(x=50,y=8)
Label(root,height=2,bg="gray").pack(side=LEFT)
Label(root,text="TICKER:",bg="gray",fg="white").place(x=3,y=8)
Label(root,text="START DATE:",bg="gray",fg="white").place(x=135+11,y=8)
Label(root,text="END DATE:",bg="gray",fg="white").place(x=296,y=8)
sts_entry = Entry(root,textvariable=start_date,width=10)
sts_entry.place(x=210+11,y=8)
#start_date.set("{}/{}/{}".format(previous.year,previous.month,previous.day))
end_datee = Entry(root,textvariable=end_date,width=10)
end_datee.place(x=362,y=8)
#end_date.set("{}/{}/{}".format(now.year,now.month,now.day))
btnHigh = Button(root,text="High",bg="gray83",width=5)
btnHigh.place(x=450,y=5)
btnLow = Button(root,text="Low",bg="gray83",width=5)
btnLow.place(x=497,y=5)
btnOpen = Button(root,text="Open",bg="gray83",width=5)
btnOpen.place(x=544,y=5)
btnClose = Button(root,text="Close",bg="light green",width=5)
btnClose.place(x=591,y=5)
btnMA50 = Button(root,text="MA 50",bg="gray83",width=8)
btnMA50.place(x=650,y=5)
btnMA200 = Button(root,text="MA 200",bg="gray83",width=8)
btnMA200.place(x=716,y=5)
Button(root,text="SHOW INFO",bg="gray83").pack(side="right",padx=2)
Button(root,text="SHOW TABLE",bg="gray83").pack(side="right",padx=2)
Button(root,text="SHOW GRAPH",bg="gray83").pack(side="right",padx=2)

#ani = animation.FuncAnimation(fig, represent, interval=1000)
buttons = {"High":btnHigh,"Low":btnLow,"Open":btnOpen,"Close":btnClose,"MA_50":btnMA50,"MA_200":btnMA200}

root.mainloop()
