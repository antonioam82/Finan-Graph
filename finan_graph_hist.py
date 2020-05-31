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
        self.more_info = Button(self.ventana,text="SHOW TABLE",state='disabled',command=self.table)
        self.more_info.pack(side=RIGHT)
        self.graph = Button(self.ventana,text="SHOW GRAPH",command=self.activate,height=1)
        self.graph.pack(side=RIGHT)
        self.btnTech = Button(self.ventana,text="BBbands",heigh=1,command=self.bands)
        self.btnTech.place(x=495,y=5)
        self.labelInfo = Label(self.ventana,text="INFO:",bg="light blue")
        self.labelInfo.place(x=290,y=8)
        self.btnH=Button(self.ventana,text="High",bg="gray83",command=lambda:self.select_items("High"))
        self.btnH.place(x=325,y=5)
        self.btnL=Button(self.ventana,text="Low",bg="gray83",command=lambda:self.select_items("Low"))
        self.btnL.place(x=364,y=5)
        self.btnV=Button(self.ventana,text="Open",bg="gray83",command=lambda:self.select_items("Open"))
        self.btnV.place(x=399,y=5)
        self.btnC=Button(self.ventana,text="Close",bg="light green",command=lambda:self.select_items("Close"))
        self.btnC.place(x=441,y=5)

        self.item_list=["High","Low","Open","Close"]
        self.buttons = {"High":self.btnH,"Low":self.btnL,"Open":self.btnV,"Close":self.btnC}

        ani = animation.FuncAnimation(self.fig, self.represent, interval=1000)
  
        self.ventana.mainloop()
        

    def select_items(self,i):
        if i not in self.selected_items:
            self.selected_items.append(i)
            self.buttons[i].configure(bg="light green")
        else:
            self.selected_items.remove(i)
            self.buttons[i].configure(bg="gray83")


    def activate(self):
        self.actv = True

    def bands(self):
        ti = TechIndicators(key='MY_API_KEY',output_format='pandas')
        self.BBdata,meta_data = ti.get_bbands(symbol=self.entry.get(),interval='60min',time_period=60)
        self.table_head = 'BBbands indicator for {} stock (60 min)'.format(self.entry.get())
        self.more_info.configure(state='normal')
        self.BBdata.plot()
        plt.title(self.table_head)
        self.display_content = self.BBdata
        plt.show()

    def get_info(self):
        if self.selected_items != []:
            try:
                self.ax1.clear()
                self.ax1.grid()
                init_date = datetime.now() - timedelta(days = int(self.entry3.get()))
                self.info = pdr.get_data_yahoo(self.entry.get(),start = init_date)
                labels = self.ax1.get_xticklabels()
                plt.setp(labels,rotation=45, horizontalalignment='right')

                for item in self.item_list:
                    if item in self.selected_items:
                        self.datas.append(item)
                for i in self.datas:
                    self.ax1.plot(self.info[i])
                self.ax1.legend((self.datas),loc='upper right', shadow=False)
                self.table_head = '{} (Last {} Days)'.format(self.entry.get(),int(self.entry3.get()))
                self.ax1.set_title(self.table_head)
                self.update_symbols_file()
                self.display_content = self.info
                self.more_info.configure(state='normal')
            except:
                messagebox.showwarning("ERROR","Hubo un error al realizar la operación")
        else:
            messagebox.showwarning("DATOS INSUFICIENTES","Especificar información a mostrar")
        self.actv = False
        self.datas = []

    def update_symbols_file(self):
        if not self.entry.get() in self.used_symbols:
            self.used_symbols.insert(0,self.entry.get())
            pickle.dump(self.used_symbols,open("symbols","wb"))
            self.entry["values"]=pickle.load(open("symbols","rb"))

    def table(self):
        top = Toplevel()
        top.title("INFO TABLE")
        self.display = sct.ScrolledText(master=top,width=80)
        self.display.pack(padx=0,pady=0)
        self.display.insert(END,self.table_head+"\n\n"+str(self.display_content))

    def represent(self,i):
        if self.actv == True:
            self.get_info()        


if __name__=="__main__":
    app()        
        
