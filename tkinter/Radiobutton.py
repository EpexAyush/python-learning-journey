import tkinter as tk
from tkinter import ttk

window=tk.Tk()

#title
window.title("Radio Button")

#window size
window.minsize(width=500,height=500)

#label
label=ttk.Label(text="Select Your Gender")
label.pack()

#Radio_Button
radio_value=tk.StringVar()

option_1=ttk.Radiobutton(text="Male",variable="radio_value",value="male")
option_2=ttk.Radiobutton(text="Female",variable="radio_value",value="Female")
option_1.pack()
option_2.pack()

window.mainloop()