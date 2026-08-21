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


