import tkinter as tk
from tkinter import ttk




window=tk.Tk()

window.title("Entry Component")
window.minsize(width=300, height=300)

label=ttk.Label(text="Enter any text")
label.pack()
User_input=ttk.Entry(width=30, show="*")
User_input.pack()

button=ttk.Button(text="Click Here")
button.pack()

window.mainloop()
