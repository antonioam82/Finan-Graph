import pandas_datareader as pdr
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import pickle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter.scrolledtext as sct
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

class app:
    def __init__(self):
        self.root = Tk()
        self.root.title("Crypto Graph")
        self.root.geometry("1070x800")
        self.root.configure(background="light green")
        self.symbol_entry = StringVar()
        self.market_entry = StringVar()
        self.used_symbolsC = pickle.load(open("symbolsC","rb"))
        self.usedsymbolsM = pickle.load(open("markets","rb"))

        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.grid()

        self.canvas = FigureCanvasTkAgg(self.fig,master=self.root)
        self.canvas.draw()
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=1)

        self.labelSym = Label(self.root,text="Symbol:",bg="light green",width=8,height=2)
        self.labelSym.pack(side=LEFT)

        self.entry = ttk.Combobox(self.root,width=8)
        self.entry["values"]=self.used_symbolsC
        self.entry.pack(side=LEFT)

        self.labelMarket = Label(self.root,text="Market:",bg="light green",width=8,height=2)
        self.labelMarket.pack(side=LEFT)
        self.entryMarket = ttk.Combobox(self.root,width=8)
        self.entryMarket["values"]=self.usedsymbolsM
        self.entryMarket.pack(side=LEFT)
        self.btnTable = Button(self.root,text="SHOW TABLE",height=1)
        self.btnTable.pack(side=RIGHT)
        self.btnGraph = Button(self.root,text="SHOW GRAPH",height=1)
        self.btnGraph.pack(side=RIGHT)
        

        self.root.mainloop()

if __name__=="__main__":
    app()


