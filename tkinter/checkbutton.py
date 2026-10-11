import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Checkbutton")


check_option=tk.StringVar()

def check_option_task():
    print(check_option.get())

check_button=ttk.Checkbutton(text="Agree with the terms & conditions",variable=check_option, command=check_option_task, onvalue="Yes",offvalue="No")
check_button.pack()








window.mainloop()