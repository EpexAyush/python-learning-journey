import tkinter as tk



window=tk.Tk()

window.title("Entry Component")
window.minsize(width=300, height=300)

label=tk.Label(text="Enter any text")
label.pack()
User_input=tk.Entry(width=30, show="*")
User_input.pack()

button=tk.Button(text="Click Here")
button.pack()

window.mainloop()
