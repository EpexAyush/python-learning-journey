import tkinter as tk
import tkinter.font as tfont


window=tk.Tk()


window.title("My Application") # for changing the title
window.minsize(width=500, height=1000) #minimum size set krega window ka


label=tk.Label(text="Hello, This is my 1st text in this GUI Application.")
label.pack()

label=tk.Label(text="Have a nice day!") # for write text in the body of the GUI Application
label.pack() #text to display karne ke liye GUI Application me

custom_font=tfont.Font(family="Times New Roman",size=15, slant="italic", weight="bold")
label=tk.Label(text="Hello this is a 3rd statement",font=custom_font)
label.pack()
#agar mujhe label ke pack hone ke baad font change karna hai to mai sirf ye krunga packing ke baad
label=tk.Label(text="This is the 4th statement.")
label.pack()
label.config(font=("Times New Roman",14,"bold","italic"))


window.mainloop()