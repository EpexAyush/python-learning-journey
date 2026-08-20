print("-----------Question:11-------------")
#we are printing the characters of a strings one by one using for loop.
word="PYTHON"
for char in word:
    print(char)

print("\n")

print("-----------Question:12-------------")
#We are taking an input from user as a string
word=input("Write any random word: ")
for char in word:
    #now we are printing the every character from the string one by one.
    print(char.upper())

print("\n")

print("-----------Question:13-------------")
#We are taking and input from the user as a string
word=input("Write any random word: ")
count=0
for i in word:
    count+=1 #counting how many times loop will run
print(f"Output is: {count}")

print("\n")
print("-----------Question:14-------------")
word="programming"
count=0
for i in word:
    if i=="g":
        count+=1
print(f"Output is: {count}")

print("\n")

print("-----------Question:15-------------")
rand_word=input("Enter a random word: ")
count=0
for i in rand_word:
    if i=="a":
        count+=1
    elif i=="e":
        count+=1
    elif i=="i":
        count+=1
    elif i=="o":
        count+=1
    elif i=="u":
        count+=1
print(f"Output is: {count}")