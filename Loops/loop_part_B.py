print("-----------Question:6-------------")
#calculating the sum from numbers 1 to 50.
total=0
for numbers in range(1,51):
    total+=numbers
print("Total:",total)

print("\n")

print("-----------Question:7-------------")
#generating sqaure of a numbers from 1 to 10.
for num in range(1,11):
    print(f"Square of {num} is: {num**2}")

print("\n")

print("-----------Question:8-------------")
#generating a multiplication table based on a user input.
user_input=int(input("Enter a random number: "))
for rand_num in range(1,11,1):
    print(f"{user_input} x {rand_num} = {rand_num*user_input}")

print("\n")

print("----------Question:9--------------")
#print numbers from 1 to 100 in descending order.
for i in range(100,0,-1):
    print(i)

print("\n")

print("------------Question:10------------")
#print those number from 1 to 100 which are only divisible by 5.
print("Numbers which are divisible by 5 are:")
for i in range(1,101,1):
    if i%5==0:
        print(i)
