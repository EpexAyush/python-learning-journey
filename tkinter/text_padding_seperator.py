import dis
import tkinter as tk
from tkinter import ttk
from turtle import fill, window_width

window=tk.Tk()
window.title("Text Padding & Seperator")
window.minsize(width=500,height=500)

label=ttk.Label(text="Write Anything Below:",padding=15)
label.pack()
sep=ttk.Separator(orient="horizontal")
sep.pack(fill="x")
text=tk.Text(width=25, height=5)
text.pack(pady=10)
text.focus()
text.insert(index=1.0,chars="Type anything")

sep=ttk.Separator(orient="horizontal")
sep.pack(fill="x")
text["state"]="disabled"

text.get(index1="1.0",index2="end")

def enable_button():
    text["state"]="normal"

enable_button=ttk.Button(text="Enable Text",command=enable_button)
enable_button.pack(pady=10)

sep=ttk.Separator(orient="horizontal")
sep.pack(fill="x")

def disable_button():
    text["state"]="disabled"

disable_button=ttk.Button(text="Disable Text",command=disable_button)
disable_button.pack(pady=10)

window.mainloop()