print("---------Question:1------------")
#We are printing numbers from 1 to 10 using for loop
for i in range(1,11,1):
    print(i)

print("\n")

print("---------Question:2------------")
#printing even numbers from 1 to 20.
num1=0
for i in range(1,21,2):
    num1+=1
    print(f"Even number {num1} is:{i+1} ")

print("\n")

print("---------Question:3------------")
#printing odd number in range 1 to 20.
num2=0
for i in range(1,20,2):
    num2+=1
    print(f"Odd number {num2} is: {i}")

print("\n")

print("---------Question:4------------")
x=int(input("Enter a number: "))
for num in range(1,x+1):
    print(num)

print("\n")

print("---------Question:5------------")
numbers= [10,25,7,42,18,31]
for element in numbers:
    print(element)