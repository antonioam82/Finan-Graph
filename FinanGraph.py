#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import pandas_datareader as pdr
from datetime import datetime, timedelta
from math import *

ventana = tkinter.Tk()
ventana.wm_title("Precio acciones")
espacio=ventana.geometry("1000x700")

tkinter.mainloop()
