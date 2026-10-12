import tkinter as tk
from tkinter import ttk


window=tk.Tk()

window.title("Checkbox and Listbox")
window.minsize(width=400,height=400)

label=tk.Label(text="Select any country from the list")
label.pack(pady=10)

#Combobox
selected_country=tk.StringVar()
countries= ttk.Combobox(textvariable=selected_country, values=("Australia","Canada","India","Sweden","North America","South Korea"))
countries["state"]="readonly"
countries.pack()

#display country 

def display_country(event):
    country_label= ttk.Label(text=selected_country.get())
    country_label.pack()
    print(f"Selected Country is {selected_country.get()}")

countries.bind("<<ComboboxSelected>>",display_country)


#ListBox
food_items= ("Pizza","Burger","Garlic bread","Nachos","Salad")
fav_food=tk.StringVar(value=food_items)

food_list=tk.Listbox(listvariable=fav_food,height=5,selectmode="extended")
food_list.pack(pady=10)


window.mainloop()