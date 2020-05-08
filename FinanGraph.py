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
canvas.get_tk_widget().pack(side=tkinter.BOTTOM,fill=tkinter.BOTH, expand=1)

entry = tkinter.Entry(master=ventana,width=30)
entry.pack(side=tkinter.LEFT)

plt.show()

tkinter.mainloop()
