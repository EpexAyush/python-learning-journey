import tkinter as tk
import tkinter.font as tfont

window=tk.Tk()

#Title
window.title("Button & Change Label Text")

#Size
window.minsize(width=200,height=200)

#Text
label=tk.Label(text="Statement 1")
label.pack()

#now i want to change the label="Statement 1 " [two methods]
label.config(text="Changed statement 1 through method 1")
#label["text"]="Changed statement 1 though method 2"


#buttons

def function_name():
    print("Thanks for clicking!")

button=tk.Button(text="Click here",command=function_name)
button.pack()

count=0
def button_click_count():
    global count
    count+=1
    label["text"]=f"Button clicked {count} times."
label=tk.Label(text=f"Button click count.")
label.pack()
button=tk.Button(text="click",command=button_click_count)
button.pack()

window.mainloop()