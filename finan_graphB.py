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
import numpy as np

class app:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Finan Graph")
        self.ventana.geometry("1070x800")
        self.ventana.configure(background="light blue")
        self.symbol_entry = StringVar()
        self.time_range = IntVar()
        self.actv = False
        self.used_symbols = pickle.load(open("symbols","rb"))
        self.datas = []
        self.selected_items = ["Close"]
        self.info = []
        self.table_head = ""
        self.display_content = ""

        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.grid()

        self.canvas = FigureCanvasTkAgg(self.fig,master=self.ventana)
        self.canvas.draw()

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.ventana)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=1)

        self.labelSym = Label(self.ventana,bg="light blue",text="Symbol:",width=8,height=2)
        self.labelSym.pack(side=LEFT)

        self.entry = ttk.Combobox(self.ventana,width=8)
        self.entry["values"]=self.used_symbols
        self.entry.pack(side=LEFT)
        self.labelRange = Label(self.ventana,text="Time (days):",bg="light blue",width=13,height=2)
        self.labelRange.place(x=135,y=0)
        self.entry3 = Entry(self.ventana,width=8,textvariable=self.time_range)
        self.entry3.place(x=220,y=8)
        self.more_info = Button(self.ventana,text="SHOW TABLE",state='disabled')
        self.more_info.pack(side=RIGHT)
        self.graph = Button(self.ventana,text="SHOW GRAPH")
        self.graph.pack(side=RIGHT)
        self.btnTech = Button(self.ventana,text="BBbands",heigh=1)
        self.btnTech.place(x=495,y=5)
        self.labelInfo = Label(self.ventana,text="INFO:",bg="light blue")
        self.labelInfo.place(x=290,y=8)
        self.btnH=Button(self.ventana,text="High",bg="gray83")
        self.btnH.place(x=325,y=5)
        self.btnL=Button(self.ventana,text="Low",bg="gray83")
        self.btnL.place(x=364,y=5)
        self.btnV=Button(self.ventana,text="Open",bg="gray83")
        self.btnV.place(x=399,y=5)
        self.btnC=Button(self.ventana,text="Close",bg="light green")
        self.btnC.place(x=441,y=5)

        self.item_list=["High","Low","Open","Close"]
        self.buttons = {"High":self.btnH,"Low":self.btnL,"Open":self.btnV,"Close":self.btnC}



        self.ventana.mainloop()

        
if __name__=="__main__":
    app() 
