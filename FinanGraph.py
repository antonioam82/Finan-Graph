import tkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

ventana = tkinter.Tk()
ventana.title("Finan Graph")
ventana.geometry("1040x700")

fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.BOTTOM,fill=tkinter.BOTH, expand=1)

labelSym = tkinter.Label(master=ventana,text="Symbol",width=8)
labelSym.pack(side=tkinter.LEFT)

entry = tkinter.Entry(master=ventana,width=8)
entry.pack(side=tkinter.LEFT)

plt.show()

tkinter.mainloop()
