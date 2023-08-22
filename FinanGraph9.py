#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import ta
from ta.utils import dropna
import yfinance as yf
import tkinter as tk
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
root = tk.Tk()
root.title("Finan Graph 8")
root.configure(background="gray")
root.geometry("1270x800")
start_date = tk.StringVar()
end_date = tk.StringVar()
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
canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH, expand=1)

# This functionality is currently not available due to a problem with the yahoo finance API.
'''def show_info():
    if tick_entry.get() != "":
        try:
            tic = yf.Ticker(tick_entry.get())
            topp = tk.Toplevel()
            topp.title("MORE INFO")
            display = sct.ScrolledText(master=topp,width=95,height=30)
            display.pack(padx=0,pady=0)
            display.insert(tk.END,"COLLECTING INFO...")
            final = tic.info
            display.delete('1.0',tk.END)
            display.insert(tk.END,tick_entry.get()+"\n\n")
            for key, value in final.items():
                display.insert(tk.END,key+":"+"\n"+str(value)+"\n\n")
        except Exception as e:
            messagebox.showwarning("UNEXPECTED ERROR",str(e))
    else:
        messagebox.showwarning("EMPTY","No info to show.")'''

def save_table():
    doc = filedialog.asksaveasfilename(initialdir="/",
                title="Save",defaultextension='.txt')
    if doc != "":
        with open(doc,"w") as document:
            document.write(table_head+"\n\n"+str(df))
        messagebox.showinfo("SAVED","Document saved")

def valid_date(char):
    return char in "0123456789/"
            
def show_table():
    if str(df) != "":
        if df.empty == False:
            top = tk.Toplevel()
            top.title("INFO TABLE")
            tk.Button(top,text="SAVE TABLE",command=save_table).pack(side=tk.BOTTOM)
            display = sct.ScrolledText(master=top,width=90,height=20)
            display.pack(padx=0,pady=0)
            display.insert(tk.END,table_head+"\n\n"+str(df))
        else:
            messagebox.showwarning("INVALID TICKER",str(df)+"\n"+"Enter a valid ticker.")
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
    try:
        ticker = tick_entry.get()
        interv = time_intervals.get()
        if ticker != "" and end_datee.get() != "" and sts_entry.get() != "":
            ax1.clear()
            ax1.grid()
            e_date = end_datee.get().split("/")
            s_date = sts_entry.get().split("/")
            enddate = date.datetime(int(e_date[0]),int(e_date[1]),int(e_date[2]))
            startdate = date.datetime(int(s_date[0]),int(s_date[1]),int(s_date[2]))
            print("END DATE --> ",e_date)
            #--------------------------------------------------------------------------------------------------
            df = yf.Ticker(ticker).history(start=startdate,end=enddate,interval=interv).reset_index()[['Date']+selected_items]
        
            if df.empty == False:
                df = dropna(df)
                if len(special_metrics)>0:
                    if not "Close" in selected_items:
                        selected_items.append("Close")
                        btnClose.configure(bg="light green")
                        df = yf.Ticker(ticker).history(start=startdate,end=enddate,interval=interv).reset_index()[['Date']+selected_items]
                        ax1.plot(df["Date"],df["Close"])
                    bol = ta.volatility.BollingerBands(df["Close"], window=10)
                    bol2= ta.volatility.BollingerBands(df["Close"], window=20)
                    for e in special_metrics:
                        selected_items.append(e)
                    if "M-AVG10" in selected_items:
                        df['M-AVG10'] = bol.bollinger_mavg()#media movil
                    if "M-AVG20" in selected_items:
                        df['M-AVG20'] = bol2.bollinger_mavg()#media movil
                    if "BOLL. BANDS" in selected_items:
                        selected_items.remove("BOLL. BANDS")
                        df['High Band'] = bol.bollinger_hband()#banda superior
                        selected_items.append('High Band')
                        df['Low Band'] = bol.bollinger_lband()
                        selected_items.append('Low Band')#banda inferior
                update_tickers(ticker)

                #---------------------------------------------------------------------------------------------------
                
                table_head = "{} ({}-{}) interv: {}".format(ticker,sts_entry.get(),end_datee.get(),interv)
        
                for i in selected_items:
                    if i == 'Low Band' or i == 'High Band':
                        ax1.plot(df["Date"],df[i],color="purple")
                    else:
                        ax1.plot(df["Date"],df[i])

                ax1.set_title(table_head)
                ax1.legend(selected_items,loc='best', shadow=False)
                ax1.set_ylabel("PRICE")
                ax1.set_xlabel("DATE")
            else:
                messagebox.showwarning("INVALID TICKER",str(df)+"\n"+"Enter a valid ticker.")
            

        else:
            messagebox.showwarning("NO TICKER OR PERIOD PROVIDED","Please, select ticker and time interval.")

    except Exception as e:
        messagebox.showwarning("UNEXPECTED ERROR",str(e))

    actv = False
    print(selected_items)
    deling = ["M-AVG10","M-AVG20","BOLL. BANDS","Low Band","High Band"]
    for i in deling:
        if i in selected_items:
            selected_items.remove(i)

    print(selected_items)
    

def activate():
    global actv
    actv = True

def update_tickers(t):
    if t not in used_symbols:
        used_symbols.insert(0,tick_entry.get())
        pickle.dump(used_symbols,open("symbols","wb"))
        tick_entry["values"]=pickle.load(open("symbols","rb"))

def init_task():
    t = threading.Thread(target=show_info)
    t.start()
    
def represent(i):
    global actv
    if actv == True:
        make_graph()

tick_entry = ttk.Combobox(root,width=10)
tick_entry["values"]=used_symbols
time_intervals = ttk.Combobox(root,width=5)
time_intervals["values"] = ["1m","2m","5m","15m","30m","60m","90m","1h","1d","5d","1wk","1mo","3mo"]
tk.Label(root,text="TICKER:",bg="gray",fg="white").pack(side=tk.LEFT)
tick_entry.pack(side=tk.LEFT)
#tk.Button(root,text="DELETE",bg="gray83").pack(side=tk.LEFT)
tk.Label(root,text="START DATE:",bg="gray",fg="white").pack(side=tk.LEFT)
validate_entry = root.register(valid_date)
sts_entry = tk.Entry(root,textvariable=start_date,width=10,validate="key",validatecommand=(validate_entry, "%S"))
sts_entry.pack(side=tk.LEFT)
tk.Label(root,text="END DATE:",bg="gray",fg="white").pack(side=tk.LEFT)
end_datee = tk.Entry(root,textvariable=end_date,width=10,validate="key",validatecommand=(validate_entry, "%S"))
end_datee.pack(side=tk.LEFT)
tk.Label(root,text="INTERVAL",bg="gray",fg="white").pack(side=tk.LEFT)
time_intervals.pack(side=tk.LEFT)
time_intervals.set("1d")

tk.Label(root,height=2,bg="gray").pack(side=tk.LEFT)
start_date.set("{}/{}/{}".format(previous.year,previous.month,previous.day))
end_date.set("{}/{}/{}".format(now.year,now.month,now.day))
btnHigh = tk.Button(root,text="High",bg="gray83",width=5,command=lambda:selection("High",selected_items))
btnHigh.place(x=579,y=5)
btnLow = tk.Button(root,text="Low",bg="gray83",width=5,command=lambda:selection("Low",selected_items))
btnLow.place(x=626,y=5)
btnOpen = tk.Button(root,text="Open",bg="gray83",width=5,command=lambda:selection("Open",selected_items))
btnOpen.place(x=673,y=5)
btnClose = tk.Button(root,text="Close",bg="light green",width=5,command=lambda:selection("Close",selected_items))
btnClose.place(x=720,y=5)#591
btnMA10 = tk.Button(root,text="MAVG 10",bg="gray83",width=12,command=lambda:selection("M-AVG10",special_metrics))
btnMA10.place(x=890-20,y=5)
btnMA20 = tk.Button(root,text="MAVG 20",bg="gray83",width=12,command=lambda:selection("M-AVG20",special_metrics))
btnMA20.place(x=966,y=5)
btnBol = tk.Button(root,text="BOLL. BANDS",bg="gray83",width=12,command=lambda:selection("BOLL. BANDS",special_metrics))
btnBol.place(x=794-20,y=5)
#tk.Button(root,text="SHOW INFO",bg="gray83",command=init_task).pack(side="right",padx=2)
tk.Button(root,text="SHOW TABLE",bg="gray83",command=show_table).pack(side="right",padx=2)
tk.Button(root,text="SHOW GRAPH",bg="gray83",command=activate).pack(side="right",padx=2)

ani = animation.FuncAnimation(fig, represent, interval=1000)
buttons = {"High":btnHigh,"Low":btnLow,"Open":btnOpen,"Close":btnClose,"M-AVG10":btnMA10,"M-AVG20":btnMA20,"BOLL. BANDS":btnBol}

root.mainloop()
