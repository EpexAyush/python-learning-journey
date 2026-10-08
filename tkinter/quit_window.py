import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Quitting Window")
window.minsize(width=500,height=500)

label=ttk.Label(text="Quitting Window")
label.pack()

button=ttk.Button(text="Click Here")
button.pack()

button=ttk.Button(text="Quit GUI Window",command=window.destroy)
button.pack()

window.mainloop()