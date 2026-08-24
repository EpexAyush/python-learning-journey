#user ka input lena hai and then check krna hai ki 1 to user_input number ke beech kitne even aur odd numbers hai 
user_input=int(input("Enter a Number: "))
i=1
count_even=0
count_odd=0
while i<=user_input:
    if i%2==0:
        count_even+=1
        i+=1
    else:
        count_odd+=1
        i+=1       
print(f"Even Numbers: {count_even}")
print(f"Odd Numbers: {count_odd}")
print("------------------------------\n")
#Divisibility Counter:
user_1=int(input("Enter a Number: "))
count_3=0
count_5=0
count_both=0
i=1
while i<=user_1:
    if i%3==0:
        count_3+=1
    if i%5==0:
        count_5+=1
    if i%3==0 and i%5==0:
        count_both+=1
    i+=1
print(f"Divisible by 3: {count_3}")
print(f"Divisible by 5: {count_5}")
print(f"Divisible by both 3 and 5: {count_both}")
print("------------------------------\n")
#Sum of Even and Odd Numbers
num=int(input("Enter a number: "))
i=1
total_even=0
total_odd=0
while i<=num:
    if i%2==0:
        total_even+=i
    else:
        total_odd+=i
    i+=1
print(f"Sum of Even Numbers: {total_even}")
print(f"Sum of Odd Numbers: {total_odd}")
print("------------------------------\n")
#Factorial of a Number
num2=int(input("Enter a Number: "))
i=num2
mul=1
while i>=1:
    mul*=i
    i-=1
print(f"Factorial of {num2}: {mul}")
print("------------------------------\n")
#Sum of Digits
user_input=input("Enter a number: ")
i=len(user_input)
index=0
total_sum=0
while index<i:
    total_sum+=int(user_input[index])
    index+=1
print(f"Total Sum of Digit: {total_sum}")
