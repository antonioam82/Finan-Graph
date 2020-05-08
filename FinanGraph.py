import tkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

ventana = tkinter.Tk()
ventana.title("Finan Graph")
ventana.geometry("1000x700")

fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP,fill=tkinter.BOTH, expand=1)

plt.show()

tkinter.mainloop()
