#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas_datareader import data as pdr
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
import warnings
warnings.filterwarnings("ignore")

if not 'symbols' in os.listdir():
    fichero = open('symbols','wb')
    pickle.dump([],fichero)
    fichero.close()

now = datetime.now()
previous = now - timedelta(days = 500)

style.use('dark_background')
root = Tk()
root.title("Finan Graph 3")
root.configure(background="gray")
root.geometry("1160x800")#1160
start_date = StringVar()
end_date = StringVar()
df = ""
table_head = ""
used_symbols = sorted(pickle.load(open("symbols","rb")))
actv = False
fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()
selected_items = ["Close"]
item_list = ["Low","High","Open","Close"]

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

def show_table():
    if str(df) != "":
        top = Toplevel()
        top.title("INFO TABLE")
        display = sct.ScrolledText(master=top,width=90,height=20)
        display.pack(padx=0,pady=0)
        display.insert(END,table_head+"\n\n"+str(df))
    else:
        messagebox.showwarning("EMPTY","No data to show.")

def selection(n):
    global selected_items
    if n not in selected_items:
        selected_items.append(n)
        buttons[n].configure(bg="light green")
    else:
        selected_items.remove(n)
        buttons[n].configure(bg="light gray")
    if selected_items == []:
        selected_items.append('Close')
        buttons['Close'].configure(bg="light green")
    print(selected_items)

def make_graph():
    global actv, df, table_head
    print("ACTIVATED")
    ticker = tick_entry.get()
    if ticker != "":
        ax1.clear()
        ax1.grid()
        enddate = date.datetime(int(end_datee.get().split("/")[0]),int(end_datee.get().split("/")[1]),int(end_datee.get().split("/")[2]))
        startdate = date.datetime(int(sts_entry.get().split("/")[0]),int(sts_entry.get().split("/")[1]),int(sts_entry.get().split("/")[2]))
        df = yf.Ticker(ticker).history(start=startdate,end=enddate).reset_index()[['Date']+selected_items]
        table_head = "{} ({}-{})".format(ticker,sts_entry.get(),end_datee.get())
        for i in selected_items:
            ax1.plot(df["Date"],df[i])
        ax1.set_title(table_head)
        ax1.legend(selected_items,loc='best', shadow=False)
        ax1.set_ylabel("PRICE")
        ax1.set_xlabel("TIME")
        #print(df.head())
    actv = False

def activate():
    global actv
    actv = True
    
def represent(i):
    global actv
    if actv == True:
        make_graph()

tick_entry = ttk.Combobox(root,width=10)
tick_entry["values"]=used_symbols
tick_entry.place(x=50,y=8)
Label(root,height=2,bg="gray").pack(side=LEFT)
Label(root,text="TICKER:",bg="gray",fg="white").place(x=3,y=8)
Label(root,text="START DATE:",bg="gray",fg="white").place(x=135+11,y=8)
Label(root,text="END DATE:",bg="gray",fg="white").place(x=296,y=8)
sts_entry = Entry(root,textvariable=start_date,width=10)
sts_entry.place(x=210+11,y=8)
start_date.set("{}/{}/{}".format(previous.year,previous.month,previous.day))
end_datee = Entry(root,textvariable=end_date,width=10)
end_datee.place(x=362,y=8)
end_date.set("{}/{}/{}".format(now.year,now.month,now.day))
btnHigh = Button(root,text="High",bg="gray83",width=5,command=lambda:selection("High"))
btnHigh.place(x=450,y=5)
btnLow = Button(root,text="Low",bg="gray83",width=5,command=lambda:selection("Low"))
btnLow.place(x=497,y=5)
btnOpen = Button(root,text="Open",bg="gray83",width=5,command=lambda:selection("Open"))
btnOpen.place(x=544,y=5)
btnClose = Button(root,text="Close",bg="light green",width=5,command=lambda:selection("Close"))
btnClose.place(x=591,y=5)
btnMA50 = Button(root,text="MA 50",bg="gray83",width=8)
btnMA50.place(x=740,y=5)
btnMA200 = Button(root,text="MA 200",bg="gray83",width=8)
btnMA200.place(x=806,y=5)
btnBol = Button(root,text="B. BANDS",bg="gray83",width=8)
btnBol.place(x=674,y=5)
Button(root,text="SHOW INFO",bg="gray83").pack(side="right",padx=2)
Button(root,text="SHOW TABLE",bg="gray83",command=show_table).pack(side="right",padx=2)
Button(root,text="SHOW GRAPH",bg="gray83",command=activate).pack(side="right",padx=2)

ani = animation.FuncAnimation(fig, represent, interval=1000)
buttons = {"High":btnHigh,"Low":btnLow,"Open":btnOpen,"Close":btnClose,"MA_50":btnMA50,"MA_200":btnMA200}

root.mainloop()
