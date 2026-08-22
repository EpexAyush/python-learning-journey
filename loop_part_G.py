#================================
#  LEVEL 1(Basic Understanding)
#================================

print("\n")

print("----------Question:1-------------")
#Skip Even numbers
num_1=[1,2,3,4,5,6,7,8,9,10]
#using for loop and continue keyword print only odd numbers
for num in num_1:
    if num%2==0:
        continue
    print(num)

print("\n")

print("-----------Question:2-------------")
#skip odd numbers
num_2=[11, 12, 13, 14, 15, 16, 17, 18]
#using for loop and continue keyword print only even numbers
for num in num_2:
    if num%2!=0:
        continue
    print(num)

print("\n")

print("------------Question:3-------------")
num_3=[10, 0, 25, 0, 8, 14, 0, 32]
for num in num_3:
    if num==0:
        continue
    print(num)

print("\n")

print("------------Question:4-------------")
num_4=[5, 12, 18, 23, 30, 42, 56, 71]
for num in num_4:
    if num==42:
        break
    print(num)

print("\n")

print("------------Question:5-------------")
#skip negative numbers using for loop and continue
num_5= [12, -5, 23, -8, 45, -2, 19]
for num in num_5:
    if num<0:
        continue
    print(num)

print("\n")

print("------------Question:6-------------")
#stop at first negative number
num_6=[12, 25, 31, 18, -7, 45, 62]
for num in num_6:
    if num<0:
        break
    print(num)

print("\n")

print("------------Question:7-------------")
#print untill 50
num_7=[10, 20, 35, 45, 50, 60, 70, 80]
for num in num_7:
    if num>50:
        break
    print(num)

print("\n")

print("------------Question:8-------------")
#skip multiples of 3
num_8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for num in num_8:
    if num%3==0:
        continue
    print(num)

print("\n")

print("------------Question:9-------------")
#Find First Number Greater Than 50
num_9=[12, 34, 28, 45, 67, 89, 23]
for num in num_9:
    if num>50:
        print(f"First number greater than 50: {num}")
        break

print("\n")

print("------------Question:10-------------")
#Search for a Student
students = ["Rahul", "Aman", "Ayush", "Riya", "Karan"]
user_input=str(input("Enter Student Name: ")).capitalize()
for stu in students:
    if stu==user_input:
        print("Student Found!")
        break
else:
    print("Student Not Found!")

print("\n")

print("------------Question:11-------------")
#First Even Number
num_11 = [13, 27, 31, 45, 52, 67, 72]
for num in num_11:
    if num%2==0:
        print(f"First Even Number is:{num}")
        break

print("\n")

print("-------------Question:12-------------")
#Skip Numbers Less Than 10
num_12 = [5, 12, 8, 20, 3, 17, 25, 7, 30]
for num in num_12:
    if num<10:
        continue
    print(num)

print("\n")

print("-------------Question:13--------------")
#sum except negative numbers
num_13=[10,-5,20,-8,15,30,-2]
total=0
for num in num_13:
    if num<0:
        continue
    total+=num
print(f"Total: {total}")

print("\n")

print("-------------Question:14---------------")
#count valid marks in between [0 to 100]
marks= [78, -5, 92, 105, 67, 88, -10, 76]
count=0
total=0
for mark in marks:
    if mark<0 or mark>100:
        continue
    count+=1
    total+=mark
print(f"Valid Marks Count: {count}")
print(f"Total Valid Marks: {total}")

print("\n")

print("------------Question:15----------------")
#stop the loop when total exceeds 100
num_15=[15, 20, 18, 25, 30, 40, 50]
total_sum=0
for num in num_15:
    total_sum+=num
    if total_sum>100:
        break
print(f"Total:{total_sum} ")

print("\n")

print("------------Question:16----------------")
#Skip Zero, Stop at Negative
num_16 = [10, 20, 0, 15, 0, 25, -5, 30, 40]
for num in num_16:
    if num==0:
        continue
    elif num<0:
        break
    print(num)

print("\n")

print("------------Question:17----------------")
#Password Attempt user ko maximum 5 attempt dene hai fir gaand maar leni hai uski..
correct_password="Python123"
for attempts in range(5,0,-1):
    user_input=input("Enter Password: ")
    if user_input==correct_password:
        print("Access Granted ✅")
        break
    else:
        print("Incorrect Password ❌")
else:
    print("Systum locked!")

print("\n")

print("-----------Question:18-----------------")
#Find First Divisible by 7
num_18= [11, 23, 34, 45, 52, 63, 71, 84]
for num in num_18:
    if num%7==0:
        print(num)
        break
print("\n")

print("-----------Question:19-----------------")
#Skip and Count negative and zeros
num_19=[12, -4, 18, 0, 25, -7, 30, 0, 45]
total=0
count=0
for num in num_19:
    if num<0:
        continue
    elif num==0:
        continue
    elif num>0:
        total+=num
        count+=1
print(f"Positive Count: {count}")  
print(f" Positive Total: {total}")

print("\n")

print("-----------Question:20----------------")
#Transaction Processing
balance=0
transactions = [500, -200, 300, 0, -100, 700, 1200, -50]
for trans in transactions:
    if balance>1000:
        break
    elif trans>0:
        balance+=trans
    elif trans<0:
        balance+=trans
    elif trans==0:
        continue
print(f"Final Balance: {balance}")
