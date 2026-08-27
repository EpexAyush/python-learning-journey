print('------------Task:1-------------\n')

def factorial(number):
    if number<=1:
        return number
    return number*factorial(number-1)

user_input=int(input("Enter a number: "))
result=factorial(user_input)
print(f"Factorial of {user_input} is: {result}")

print("\n")

print("-------------Task:2--------------\n")

import math
user_input=int(input("Enter a number: "))

print(f"Square root: {math.sqrt(user_input)}")
print(f"Logarithm: {math.log(user_input)}")
print(f"Sine: {math.sin(user_input)}")