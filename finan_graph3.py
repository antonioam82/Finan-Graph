#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas_datareader as pdr
#from alpha_vantage.techindicators import TechIndicators
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

class graph:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Finan Graph")
        self.ventana.geometry("1070x800")
        self.ventana.configure(background="light blue")
        self.fig = Figure()
        ax1 = self.fig.add_subplot(111)
        ax1.grid()
        self.actv = False
        
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.ventana)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM,fill=BOTH,expand=1)

        self.labelSym = Label(master=self.ventana,bg="light blue",text="Symbol:",width=8,height=2)
        self.labelSym.pack(side=LEFT)
        self.entry = ttk.Combobox(master=self.ventana,width=8)
        #self.entry["values"]
        self.entry.pack(side=LEFT)

        self.labelRange = Label(master=self.ventana,text="Time (days):",bg="light blue",width=13,height=2)
        self.labelRange.place(x=135,y=0)
        self.entry3 = Entry(master=self.ventana,width=8)
        self.entry3.place(x=220,y=8)
        self.more_info = Button(master=self.ventana,text="SHOW TABLE",state='disabled')
        self.more_info.pack(side=RIGHT)
        self.graph = Button(master=self.ventana,text="SHOW GRAPH",height=1,command=self.change_actv)
        self.graph.pack(side=RIGHT)
        self.typeLabel = Label(master=self.ventana,text="GRAPH TYPE:",bg="light blue")
        self.typeLabel.place(x=286,y=8)
        self.typeEntry = ttk.Combobox(master=self.ventana,state='readonly',width=12)
        self.typeEntry.place(x=365,y=8)
        self.btnTech = Button(master=self.ventana,text="BBbands",height=1)
        self.btnTech.place(x=495,y=5)
        self.labelInfo = Label(master=self.ventana,text="INFO:",bg="light blue")
        self.entry_styles = ttk.Combobox(master=self.ventana,state='readonly',width=19)
        self.entry_styles.pack(padx=3,side=RIGHT)
        #self.entry_styles.set(styl)
        self.label_styles = Label(master=self.ventana,text="STYLE:",bg="light blue")
        self.label_styles.pack(side=RIGHT)
        #self.entry_styles['values']=styles

        animat = animation.FuncAnimation(self.fig, self.repGraph, interval=1000)

        self.ventana.mainloop()

    def change_actv(self):
        if self.actv == True:
            self.actv = False
        else:
            self.actv = True
        

    def repGraph(self,i):
        if self.actv == True:
            print("None")


    
if __name__=="__main__":
    graph()
