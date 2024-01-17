#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as sct
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.animation as animation
from matplotlib import style
import threading
import os
import warnings
warnings.filterwarnings("ignore")

style.use('grayscale')
root = tk.Tk()
root.title("Finan Graph 9")
root.configure(background="gray")
root.geometry("1270x800")

fig = Figure()
ax1 = fig.add_subplot(111)
ax1.grid()

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH, expand=1)

root.mainloop()
