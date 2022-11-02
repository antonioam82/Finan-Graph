import pandas_datareader as pdr
from datetime import datetime, timedelta
import mplfinance as mpf
import pickle
import tkinter as tk
from tkinter import ttk

from tkinter import messagebox, filedialog
import tkinter.scrolledtext as sct
#import datetime as date
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
