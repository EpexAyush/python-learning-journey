# Q1: What type of literal is 45?
data_1=45
print(type(data_1))

# Q2: What type of literal is "Python"?
data_2="Python"
print(type(data_2))

# Q3. What type of literal is 99.99?
data_3= 99.99
print(type(data_3))

# Q4. What type of literal is False?
data_4= False
print(type(data_4))

# Q5. What type of literal is None?
data_5=None
print(type(data_5))



#LEVEL 2 — Application
#Objective: Write the correct literal yourself based on the requirement.
# Q1. Write a string literal representing your favorite color.
data_6="black"
print(type(data_6))

# Q2. Write an integer literal representing the number of days in a normal year.
data_7=365
print(type(data_7))

# Q3. Write a float literal representing exactly half of a dollar (e.g., 50 cents).
data_8=0.5
print(type(data_8))

# Q4. Write a boolean literal representing that a lightbulb is currently turned on.
data_9=True
print(type(data_9))

# Q5. Write a string literal that contains a number inside it (for example, a house number).
data_10="A20"
print(type(data_10))




# LEVEL 3 — Problem Solving
# Objective: Differentiate between tricky literals.

# Q1. Look at 100 and "100". Explain the difference between these two literals in plain English.
data_11= 100
data_12= "100"
print(f"{data_11} is a {type(data_11)} while \"{data_12}\" is a {type(data_12)}.")


# Q2. Look at True and "True". Are these the same type of literal? Why or why not?
data_13=True
data_14="True"
print(f'is True and "True" both are same?,{data_13==data_14} because True is a {type(data_13)} and "True" is a {type(data_14)}.')


# Q3. If you write -250, is this a valid integer literal in Python?
data_15= -250
print("Yes,This is valid intergar in python, you can check it by writting:","type(data_15)")


# Q4. How would you write a float literal for the number fifty (without changing its mathematical value)?
data_16=50.0
print(type(data_16))


# Q5. If you want to create a string literal that says: It's raining (Notice the single quote in It's), how would you write this literal so that Python doesn't get confused by the quotes?
print("it's raining.") # 1st method
print('it\'s raining.') #2nd method




# LEVEL 4 — Challenge
# Objective: Think about how Python interprets real-world data.

# Q1. In the real world, we write one million as 1,000,000. If you type 1,000,000 directly into Python, is it treated as a single integer literal? What do you think Python sees? (Take a guess!)
data_17=1,000,000
print(type(data_17)) #No it is giving tuple.


# Q2. You are recording data for a user. They have a first name and a last name, but absolutely no middle name. Which specific literal is best to represent "nothing" or "empty" in Python?
#Ans: None literal will be used




# LEVEL 5 — Mini Project
# Project Name: The Literal Character Profile

# Requirements:
# Since we haven't learned variables yet, you don't need to write a full Python script. Just provide a raw list of literals that describe a fictional character.

# You must provide exactly:
# One String literal (Their name)
print("Ayush kumar")
# One Integer literal (Their age)
print(21)
# One Float literal (Their height in meters, e.g., 1.75)
print(165.0)
# One Boolean literal (Do they have a superpower?)
print(False)
# One Special literal (Their weakness—assuming they don't have one!)
print(None)