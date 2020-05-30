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

        self.ventana.mainloop()

        
if __name__=="__main__":
    app() 
