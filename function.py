def  greet():
    print("Hello, Good Morning!")


i=1
while i<=10:
    greet()
    i+=1

#now we are defining the parameter inside the function name
def greet(name):
    print(f"Hello,{name},Good Morning!")

greet("Ayush")
greet("Shubham")
greet("Mukul")

#so we are creating a function which will print a welcome message
def welcome(name,age,city):
    print("Hello",name)
    print(f"{name}, You are {age} years old.")
    print(f"You live in {city}.")

welcome("Ayush",22,"Gurgaon")