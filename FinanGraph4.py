#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import ta
from ta.utils import dropna
import yfinance as yf
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
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
root.title("Finan Graph 4")
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
special_metrics = []

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH, expand=1)

def show_info():
    if tick_entry.get() != "":
        try:
            tic = yf.Ticker(tick_entry.get())
            topp = Toplevel()
            topp.title("MORE INFO")
            display = sct.ScrolledText(master=topp,width=95,height=30)
            display.pack(padx=0,pady=0)
            display.insert(END,"COLLECTING INFO...")
            final = tic.info
            display.delete('1.0',END)
            display.insert(END,tick_entry.get()+"\n\n")
            for key, value in final.items():
                display.insert(END,key+":"+"\n"+str(value)+"\n\n")

        except Exception as e:
            messagebox.showwarning("UNEXPECTED ERROR",str(e))
    else:
        messagebox.showwarning("EMPTY","No info to show.")

def save_table():
    doc = filedialog.asksaveasfilename(initialdir="/",
                title="Save",defaultextension='.txt')
    if doc != "":
        with open(doc,"w") as document:
            document.write(table_head+"\n\n"+str(df))
        messagebox.showinfo("SAVED","Document saved")
            
def show_table():
    if str(df) != "":
        top = Toplevel()
        top.title("INFO TABLE")
        Button(top,text="SAVE TABLE",command=save_table).pack(side=BOTTOM)
        display = sct.ScrolledText(master=top,width=90,height=20)
        display.pack(padx=0,pady=0)
        display.insert(END,table_head+"\n\n"+str(df))
    else:
        messagebox.showwarning("EMPTY","No data to show.")

def selection(n,l):
    global selected_items, special_metrics
    if n not in l:
        l.append(n)
        buttons[n].configure(bg="light green")
    else:
        l.remove(n)
        buttons[n].configure(bg="light gray")
    if selected_items == []:
        selected_items.append('Close')
        buttons['Close'].configure(bg="light green")
    print("S. Items:",selected_items)
    print("Sp. Metrics:",special_metrics)

def make_graph():
    global actv, df, table_head
    print("ACTIVATED")
    ticker = tick_entry.get()
    if ticker != "":
        ax1.clear()
        ax1.grid()
        e_date = end_datee.get().split("/")
        s_date = sts_entry.get().split("/")
        enddate = date.datetime(int(e_date[0]),int(e_date[1]),int(e_date[2]))
        startdate = date.datetime(int(s_date[0]),int(s_date[1]),int(s_date[2]))

        #--------------------------------------------------------------------------------------------------
        df = yf.Ticker(ticker).history(start=startdate,end=enddate).reset_index()[['Date']+selected_items]

        df = dropna(df)
        if len(special_metrics)>0:
            if not "Close" in selected_items:
                selected_items.append("Close")
                btnClose.configure(bg="light green")
                df = yf.Ticker(ticker).history(start=startdate,end=enddate).reset_index()[['Date']+selected_items]
                ax1.plot(df["Date"],df["Close"])
            bol = ta.volatility.BollingerBands(df["Close"], window=20)
            for e in special_metrics:
                selected_items.append(e)
            if "M-AVG" in selected_items:
                df['M-AVG'] = bol.bollinger_mavg()#media movil
            if "BOLL. BANDS" in selected_items:
                selected_items.remove("BOLL. BANDS")
                df['High Band'] = bol.bollinger_hband()#banda superior
                selected_items.append('High Band')
                df['Low Band'] = bol.bollinger_lband()
                selected_items.append('Low Band')#banda inferior
        #---------------------------------------------------------------------------------------------------
                
        table_head = "{} ({}-{})".format(ticker,sts_entry.get(),end_datee.get())
        
        for i in selected_items:
            if i == 'Low Band' or i == 'High Band':
                ax1.plot(df["Date"],df[i],color="purple")
            else:
                ax1.plot(df["Date"],df[i])

        ax1.set_title(table_head)
        ax1.legend(selected_items,loc='best', shadow=False)
        ax1.set_ylabel("PRICE")
        ax1.set_xlabel("TIME")

    else:
        messagebox.showwarning("NO TICKER","Please, select a ticker")    

    actv = False
    print(selected_items)
    deling = ["M-AVG","BOLL. BANDS","Low Band","High Band"]
    for i in deling:
        if i in selected_items:
            selected_items.remove(i)

    print(selected_items)

def activate():
    global actv
    actv = True

def init_task():
    t = threading.Thread(target=show_info)
    t.start()
    
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
btnHigh = Button(root,text="High",bg="gray83",width=5,command=lambda:selection("High",selected_items))
btnHigh.place(x=450,y=5)
btnLow = Button(root,text="Low",bg="gray83",width=5,command=lambda:selection("Low",selected_items))
btnLow.place(x=497,y=5)
btnOpen = Button(root,text="Open",bg="gray83",width=5,command=lambda:selection("Open",selected_items))
btnOpen.place(x=544,y=5)
btnClose = Button(root,text="Close",bg="light green",width=5,command=lambda:selection("Close",selected_items))
btnClose.place(x=591,y=5)
btnMA = Button(root,text="MAVG 20",bg="gray83",width=12,command=lambda:selection("M-AVG",special_metrics))
btnMA.place(x=770,y=5)
btnBol = Button(root,text="BOLL. BANDS",bg="gray83",width=12,command=lambda:selection("BOLL. BANDS",special_metrics))
btnBol.place(x=674,y=5)
Button(root,text="SHOW INFO",bg="gray83",command=init_task).pack(side="right",padx=2)
Button(root,text="SHOW TABLE",bg="gray83",command=show_table).pack(side="right",padx=2)
Button(root,text="SHOW GRAPH",bg="gray83",command=activate).pack(side="right",padx=2)

ani = animation.FuncAnimation(fig, represent, interval=1000)
buttons = {"High":btnHigh,"Low":btnLow,"Open":btnOpen,"Close":btnClose,"M-AVG":btnMA,"BOLL. BANDS":btnBol}

root.mainloop()
