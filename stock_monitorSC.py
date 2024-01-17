#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
import numpy as np

'''def generate_data():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    return x, y'''

# Función principal
def main():
    # grayscale, _classic_test, 
    # Crear la ventana principal
    style.use('dark_background')
    root = tk.Tk()
    root.title("Stock Screen")
    root.geometry("730x500")

    #x, y = generate_data()

    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.grid()
    '''plot.plot(x, y, label='Función Seno')
    plot.set_title('Gráfica de Ejemplo')
    plot.set_xlabel('Eje X')
    plot.set_ylabel('Eje Y')
    plot.legend()'''  

    # Incorporar la figura en la interfaz de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    # Iniciar el bucle principal de Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
