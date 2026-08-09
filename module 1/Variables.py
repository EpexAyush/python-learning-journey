# LEVEL 1 — Basic Understanding
# Objective: Test your knowledge of variable naming rules and basic assignment.

# Q1. Which of the following variable names are INVALID in Python, and why?
# a) user_age
# b) 2nd_player
# c) TotalScore
# d) first-name
# e) _hidden_data

'''Ans: b and d option is INVAID '''


# Q2. Python is case-sensitive. If you create a variable score = 50 and then try to print Score, what will happen?
score=50
# print(Score) #It will throw an error because of we have written capital S inside the print function while variable starts with the small letter. 


# Q3. Look at this code: 100 = max_health. Is this valid Python code? If not, what is the rule that it breaks?
# 100= max_health 
# print(100) 
#Yes, It will throw an error because you can't assign intergar literal as a variable.


# Q4. What is "Dynamic Typing" in Python? (Hint: Can a variable hold an Integer, and then later hold a String?)
#Ans: No primitive data types are immutable you can't modify it in the same memory location.



# What is the value of y? Is y holding the letter 'x' or the integer 10?
x=10
y=x
#Ans: x holding an integar 10 and y holding x which holds integar 10 so ultimately y also holds integar 10.


# LEVEL 2 — Application
# Objective: Create variables correctly and print them.

# Q1. The Book Inventory
# Create three properly named variables for a book: its title (string), its page count (integer), and its price (float). Print all three variables.
title="400 Days"
page_count=400
price=256.55
print(f"This book name is {title} and it has {page_count} pages and the price of this book is {price} INR")


# Q2. The Shape Shifter
# Create a variable named mystery_box. Assign the integer 5 to it and print it. On the next line, reassign the string "Surprise!" to the exact same variable, and print it again.
mystery_box=5
print(mystery_box)
mystery_box="Surprise!"


# Q3. The Constant Truth
# Create a variable named is_python_fun and assign the correct Boolean literal to it. Print its type to prove it is a boolean.
is_python_fun=True
print(type(is_python_fun))

# Q4. Fixing the Errors
# The following code has illegal variable names. Fix the variable names so the code runs without errors.
# my name = "Ayush"
# @age = 22
# class = "Python"
my_name= "Ayush" # do not give spaces between words
age=22  # special characters are not allowed in variables name.
language="Python" # built-in keywords are not allowed in python like class.


# Q5. Multiple Assignment
# Python allows you to assign the same value to multiple variables in one line. Try assigning the literal 0 to three variables: player1_score, player2_score, and player3_score using a single line of code.
player1_score=player2_score=player3_score=0
print(player1_score,player2_score,player3_score)


# LEVEL 3 — Problem Solving
# Objective: Trace how data moves between variables in memory.

# Q1. The Memory Trace
# Read the code below. What will be printed at the end? (Do not run it in VS Code yet, trace it in your mind first!)
a = 15
b = a
a = 30
print(b) #Ans: 15


Q2. The Swap (Without Math)
You have two glasses.
glass_a = "Milk"
glass_b = "Water"
empty_glass=glass_a #empty glass ke andr humne milk daal diyaa
glass_a= glass_b #ab glass a me water bhara hua hai 
glass_b= empty_glass #ab glass b me milk daal diyaa 
print(f"The GLASS A has: {glass_a} and The GLASS B has {glass_b}")



# Q3. Best Practices (PEP 8)
# You want to create a variable for a bank account balance. Which of these three is the most "Pythonic" way to name it, and what is this naming style called?
# a) BankAccountBalance = 1000
# b) bankAccountBalance = 1000
# c) bank_account_balance = 1000 #option c is best


# Q4. The Missing Data
# You are creating a variable for a user's profile picture, but the user hasn't uploaded one yet. What literal should you assign to the profile_picture variable to represent "nothing"?
user_profile_picture=None

# What does color1 print, and why?
color1 = "Blue"
color2 = "Red"
color1 = color2
color2 = "Green"
print(color1) #it will print red colour


# LEVEL 4 — Challenge
# Objective: Think logically about state changes over time.

# Q1. The Game State
# Imagine you are building a text-based game.
# Create a variable hero_health and set it to 100.
# The hero takes damage. (Since we don't know math operators yet, simply reassign hero_health to 80).
# The hero finds a health potion. Reassign it to 100.
# The hero falls into a trap and loses all health. Reassign it to a literal that represents absolute zero or nothingness (not the number 0).
# Print the hero_health variable after every single event.
hero_health=100
print(hero_health)
hero_health=80
print(hero_health)
hero_health=100
print(hero_health)
hero_health=None
print(hero_health)


# Q2. The Vault Password
vault_code = 1234
fake_code = vault_code
vault_code = 9999
# If a hacker steals the fake_code variable, what number do they get? Explain why changing vault_code to 9999 did not update fake_code.
#Ans: 1234 i think code runs from top to bottom but i dont know exact the code flow abhi ye sab nhi padhaya hai


# LEVEL 5 — Mini Project
# Project Name: The Digital Student ID Card
# Requirements:
# Write a Python script that creates a digital ID card for a student (you can use your own details!).
# You must define the following variables, making sure your variable names follow perfect Python naming conventions (snake_case):
# First Name
# Last Name
# Age
# Course Name (e.g., Data Science or NPTEL Python)
# Current GPA / Percentage (Float)
# Is Enrolled (Boolean)
# After defining all the variables, use print() to display each variable one by one so it looks like an ID card is being printed out.

first_name="AYUSH"
last_name="KUMAR"
age=21
course_name="BS computer Sciencec and Data Analytics"
current_cgpa=None
is_enrolled=True
print(f"Name: {first_name} {last_name}")
print(F"Age: {age}")
print(f"Course: {course_name}")
print(f"Current Cgpa: {current_cgpa}")
print(f"ID Active Status: {is_enrolled}")