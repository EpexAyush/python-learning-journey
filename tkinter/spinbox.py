import tkinter as tk
from tkinter import Spinbox, ttk

window=tk.Tk()
window.title("Spinbox")
window.minsize(width=400,height=400)

counter=tk.IntVar(value=10)
spin_box=ttk.Spinbox(from_=0, to=20, textvariable=counter,wrap=True)
spin_box.pack()

print(spin_box.get())

window.mainloop()