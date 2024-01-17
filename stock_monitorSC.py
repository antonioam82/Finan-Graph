import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# Función principal
def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Stock Screen")
    root.geometry("730x500")

    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    plot.grid()

    # Incorporar la figura en la interfaz de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    # Iniciar el bucle principal de Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
