from math import exp
import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Frames & Background Colors")
#window.minsize(width=500,height=500)

my_frame=ttk.Frame()
my_frame.pack(side="left",fill="both",expand=True)


label1=tk.Label(my_frame,text="Hello World",bg="red")
label1.pack(side="left",fill="both",expand=True)

label2=tk.Label(text="How are you?",bg="green")
label2.pack(side="top",fill="both",expand=True)

label3=tk.Label(text="What are you doing?",bg="yellow")
label3.pack(side="top",fill="both",expand=True)


window.mainloop()