#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from pandas_datareader import data as pdr
import pickle
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
import os
#import mplfinance as mpf
import numpy as np

#if not 'symbols' in os.listdir():
 if not os.path.exists("symbols"):  
    fichero = open('symbols','wb')
    pickle.dump([],fichero)
    fichero.close()

now = datetime.now()
previous = now - timedelta(days = 500)

style.use('dark_background')
root = Tk()
root.title("Finan Graph 5")
root.configure(background="gray")
root.geometry("1160x800")
start_date = StringVar()
end_date = StringVar()
balance = StringVar()
df2 = ""
table_head = ""
used_symbols = sorted(pickle.load(open("symbols","rb")))
actv = False
fig = Figure()
ax1 = fig.add_subplot(111)
ax1.set_ylabel("PRICE")
ax1.set_xlabel("TIME")
ax1.grid()
selected_items = ["Close"]
item_list = ["Low","High","Open","Close","EMA_50","EMA_200"]

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

def activate():
    global actv
    actv = True

def show_table():
    if str(df2) != "":
        top = Toplevel()
        top.title("INFO TABLE")
        display = sct.ScrolledText(master=top,width=90,height=20)
        display.pack(padx=0,pady=0)
        display.insert(END,table_head+"\n\n"+str(df2))
    else:
        messagebox.showwarning("EMPTY","No data to show.")


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

def validate_date(l):
    if int(l[2]) <= 1 and int(l[1]) <= 1 and int(l[0]) <= 1970:
        return None
    else:
        return l
        
def make_graph():
    try:
        global actv, df2, table_head
        variables = []
        ax1.clear()
        ax1.grid()
        end_list= validate_date(end_datee.get().split("/"))
        start_list= validate_date(sts_entry.get().split("/"))

        if end_list is not None and start_list is not None:
            enddate = date.datetime(int(end_list[0]),int(end_list[1]),int(end_list[2]))
            startdate = date.datetime(int(start_list[0]),int(start_list[1]),int(start_list[2]))
            tick = tick_entry.get()
            yf.pdr_override()
            ipc = pdr.get_data_yahoo(tick, start = startdate, end = enddate)
            difer ="{:.2f}".format(ipc['Close'][-1]-ipc['Close'][-2])
            balance.set(difer)
            if float(difer)<0:
                diferEntry.configure(fg='red')
            else:
                diferEntry.configure(fg='light green')
            #print("MY INFO: ",ipc)
            if not "Empty DataFrame" in str(ipc):
                df = EMA(ipc, 50)
                df2 = EMA(df, 200)
                for i in item_list:
                    if i in selected_items:
                        variables.append(i)
                df2 = df2[variables]
                for i in df2:
                    ax1.plot(df2[i])
                ax1.legend(variables,loc='best', shadow=False)
                ax1.set_ylabel("PRICE")
                ax1.set_xlabel("DATES")
                table_head = "{} ({}-{})".format(tick,sts_entry.get(),end_datee.get())
                ax1.set_title(table_head)
                update_tickers(tick)
            else:
                messagebox.showwarning("NO DATA",str(ipc))
        else:
            messagebox.showwarning("ERROR","Bad date")
        
    except Exception as e:
        messagebox.showwarning("UNEXPECTED ERROR",str(e))
    actv = False

def update_tickers(t):
    if t not in used_symbols:
        used_symbols.insert(0,tick_entry.get())
        pickle.dump(used_symbols,open("symbols","wb"))
        tick_entry["values"]=pickle.load(open("symbols","rb"))
    
def represent(i):
    global actv
    if actv == True:
        make_graph()

tick_entry = ttk.Combobox(root,width=10)
tick_entry["values"]=used_symbols
tick_entry.place(x=50,y=8)
diferEntry = Entry(root,textvariable=balance,width=10,bg='black')
diferEntry.place(x=145,y=8)
Label(root,height=2,bg="gray").pack(side=LEFT)
Label(root,text="TICKER:",bg="gray",fg="white").place(x=3,y=8)
Label(root,text="START DATE:",bg="gray",fg="white").place(x=246,y=8)
Label(root,text="END DATE:",bg="gray",fg="white").place(x=396,y=8)
sts_entry = Entry(root,textvariable=start_date,width=10)
sts_entry.place(x=321,y=8)
start_date.set("{}/{}/{}".format(previous.year,previous.month,previous.day))
end_datee = Entry(root,textvariable=end_date,width=10)
end_datee.place(x=462,y=8)
end_date.set("{}/{}/{}".format(now.year,now.month,now.day))
btnHigh = Button(root,text="High",bg="gray83",command=lambda:selection("High"),width=5)
btnHigh.place(x=550,y=5)
btnLow = Button(root,text="Low",bg="gray83",command=lambda:selection("Low"),width=5)
btnLow.place(x=597,y=5)
btnOpen = Button(root,text="Open",bg="gray83",command=lambda:selection("Open"),width=5)
btnOpen.place(x=644,y=5)
btnClose = Button(root,text="Close",bg="light green",command=lambda:selection("Close"),width=5)
btnClose.place(x=691,y=5)
btnEMA50 = Button(root,text="EMA 50",bg="gray83",command=lambda:selection("EMA_50"),width=8)
btnEMA50.place(x=750,y=5)
btnEMA200 = Button(root,text="EMA 200",bg="gray83",command=lambda:selection("EMA_200"),width=8)
btnEMA200.place(x=816,y=5)
Button(root,text="SHOW TABLE",bg="gray83",command=show_table).pack(side="right",padx=2)
Button(root,text="SHOW GRAPH",bg="gray83",command=activate).pack(side="right",padx=2)

ani = animation.FuncAnimation(fig, represent, interval=1000)
buttons = {"High":btnHigh,"Low":btnLow,"Open":btnOpen,"Close":btnClose,"EMA_50":btnEMA50,"EMA_200":btnEMA200}
root.mainloop()
