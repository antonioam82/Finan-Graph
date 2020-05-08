import tkinter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

ventana = tkinter.Tk()
ventana.title("Finan Graph")
ventana.geometry("1040x700")
ventana.configure(background="light blue")

fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.BOTTOM,fill=tkinter.BOTH, expand=1)

labelSym = tkinter.Label(master=ventana,bg="light blue",text="Symbol:",width=8)
labelSym.pack(side=tkinter.LEFT)
entry = tkinter.Entry(master=ventana,width=8)
entry.pack(side=tkinter.LEFT)
labelCom = tkinter.Label(master=ventana,bg="light blue",text="Compare with:",width=10)
labelCom.place(x=153,y=0)
entry2 = tkinter.Entry(master=ventana,width=8)
entry2.place(x=240,y=1)

plt.show()

tkinter.mainloop()
