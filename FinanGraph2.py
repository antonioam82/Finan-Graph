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

def define_date(n):
    def new_date(st):
        if st == 'start':
            start_date.set(cal.get_date())
        else:
            end_date.set(cal.get_date())
            
    top = Toplevel()
    top.title("SET DATE")
    cal = Calendar(top,selectmode="day",year=2021,month=6,day=22)
    cal.pack(pady=20)
    Label(top,text=cal.get_date()).pack(side='bottom')
    Button(top,text="SET DATE",command=lambda:new_date(n)).pack(side='bottom')

    top.mainloop()

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
Button(root,text="START DATE",command=lambda:define_date("start")).place(x=135+11,y=5)
Button(root,text="END DATE",width=8,command=lambda:define_date("end")).place(x=316+11,y=5)
sts_entry = Entry(root,textvariable=start_date,font=('arial',13),width=10)
sts_entry.place(x=210+11,y=5)
end_datee = Entry(root,textvariable=end_date,font=('arial',13),width=10)
end_datee.place(x=382+11,y=5)
btnHigh = Button(root,text="High",width=5)
btnHigh.place(x=450+60,y=5)
btnLow = Button(root,text="Low",width=5)
btnLow.place(x=497+60,y=5)
btnOpen = Button(root,text="Open",width=5)
btnOpen.place(x=544+60,y=5)
btnClose = Button(root,text="Close",width=5)
btnClose.place(x=591+60,y=5)
btnEMA50 = Button(root,text="EMA 50",width=8)
btnEMA50.place(x=650+60,y=5)
btnEMA200 = Button(root,text="EMA 200",width=8)
btnEMA200.place(x=776,y=5)
Button(root,text="SHOW GRAPH",command=activate).place(x=950,y=5)
    

def EMA(df, n):
    EMA = pd.Series(pd.Series.ewm(df['Close'],span = n, min_periods = n-1, adjust=False).mean(), name='EMA_'+str(n))
    df = df.join(EMA)
    return df

def make_graph():
    global actv
    ax1.clear()
    ax1.grid()
    enddate = date.datetime(end_datee.get())
    print(enddate)
    startdate = date.datetime(sts_date.get())
    tick = tick_entry.get()
    ipc = pdr.get_data_yahoo(tick, start = startdate, end = enddate)
    df = EMA(ipc, 50)
    df2 = EMA(df, 200)
    df2 = df2[['Close','EMA_50','EMA_200']]#['High','Low','Open','Close','EMA_50','EMA_200']]
    for i in df2:
        ax1.plot(df2[i])
    ax1.legend(['Close','EMA_50','EMA_200'],loc='best', shadow=False)
    actv = False
    
def represent(i):
    global actv
    if actv == True:
        make_graph()

ani = animation.FuncAnimation(fig, represent, interval=1000)
root.mainloop()

