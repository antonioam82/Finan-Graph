#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
import numpy as np

def main():
    # Crear la ventana principal
    style.use('dark_background')
    root = tk.Tk()
    root.title("Stock Screen")
    root.geometry("730x500")

    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.grid()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    root.mainloop()

if __name__ == "__main__":
    main()
