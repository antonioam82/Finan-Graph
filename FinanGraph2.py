#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas_datareader import data as pdr
from tkcalendar import *
import pickle
from tkinter import *
from tkinter import ttk
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



def activate():
    global actv
    actv = True

#style.use('dark_background')
root = Tk()
root.title("Finan Graph 5")
root.configure(background="gray")
root.geometry("1160x800")#1160
start_date = StringVar()
end_date = StringVar()
used_symbols = pickle.load(open("symbols","rb"))
actv = False
fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()
selected_items = []
item_list = ["Low","High","Open","Close","EMA_50","EMA_200"]


canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

tick_entry = ttk.Combobox(root,width=8)
tick_entry["values"]=used_symbols
tick_entry.set('IBM')
tick_entry.place(x=58,y=8)
Label(root,height=2,bg="gray").pack(side=LEFT)
Label(root,text="TICKER:",bg="gray",fg="white").place(x=10,y=8)
Label(root,text="START DATE:",bg="gray",fg="white").place(x=135+11,y=8)
Label(root,text="END DATE:",bg="gray",fg="white").place(x=296,y=8)
sts_entry = Entry(root,textvariable=start_date,width=10)
sts_entry.place(x=210+11,y=8)
end_datee = Entry(root,textvariable=end_date,width=10)
end_datee.place(x=362,y=8)
btnHigh = Button(root,text="High",command=lambda:selection("High"),width=5)
btnHigh.place(x=450,y=5)
btnLow = Button(root,text="Low",command=lambda:selection("Low"),width=5)
btnLow.place(x=497,y=5)
btnOpen = Button(root,text="Open",command=lambda:selection("Open"),width=5)
btnOpen.place(x=544,y=5)
btnClose = Button(root,text="Close",command=lambda:selection("Close"),width=5)
btnClose.place(x=591,y=5)
btnEMA50 = Button(root,text="EMA 50",command=lambda:selection("EMA_50"),width=8)
btnEMA50.place(x=650,y=5)
btnEMA200 = Button(root,text="EMA 200",command=lambda:selection("EMA_200"),width=8)
btnEMA200.place(x=716,y=5)
Button(root,text="SHOW GRAPH",command=activate).place(x=950,y=5)
    

def EMA(df, n):
    EMA = pd.Series(pd.Series.ewm(df['Close'],span = n, min_periods = n-1, adjust=False).mean(), name='EMA_'+str(n))
    df = df.join(EMA)
    return df

def selection(n):
    global selected_items
    if n not in selected_items:
        selected_items.append(n)
        buttons[n].configure(bg="light green")
    else:
        selected_items.remove(n)
        buttons[n].configure(bg="light gray")
        

def make_graph():
    global actv
    variables = []
    ax1.clear()
    ax1.grid()
    end_list=(end_datee.get().split("/"))#2019,11,1
    start_list=(sts_entry.get().split("/"))#2010,1,1
    
    enddate = date.datetime(int(end_list[0]),int(end_list[1]),int(end_list[2]))
    startdate = date.datetime(int(start_list[0]),int(start_list[1]),int(start_list[2]))
    tick = tick_entry.get()
    ipc = pdr.get_data_yahoo(tick, start = startdate, end = enddate)
    df = EMA(ipc, 50)
    df2 = EMA(df, 200)
    for i in item_list:
        if i in selected_items:
            variables.append(i)
    df2 = df2[variables]
    for i in df2:
        ax1.plot(df2[i])
    ax1.legend(variables,loc='best', shadow=False)
    print(variables)
    actv = False
    
def represent(i):
    global actv
    if actv == True:
        make_graph()

ani = animation.FuncAnimation(fig, represent, interval=1000)
buttons = {"High":btnHigh,"Low":btnLow,"Open":btnOpen,"Close":btnClose,"EMA_50":btnEMA50,"EMA_200":btnEMA200}
root.mainloop()
