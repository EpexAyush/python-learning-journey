print("-----------Question:18-------------")
#calculating the total of the number using for loop. 
#do not use sum() function.
numbers = [15, 28, 7, 34, 19, 42]
total=0
for i in numbers:
    total=total+i
print(f"Total: {total}")

print("\n")

print("-----------Question:19-------------")
#finding the highest number using for loop.
# do not use max() function here.
numbers = [23, 67, 12, 89, 45, 31]
highest=numbers[0] #23
for high in numbers:
    if high>highest:
        highest=high
print(f"Highest number is: {highest}")

print("\n")

print("-----------Question:20-------------")
#finding the minimum number using for loop.
# do not use min() function here.
numbers = [56, 14, 78, 3, 91, 27]
lowest=numbers[0]
for i in numbers:
    if i<lowest:
        lowest=i
print(f"Lowest Number is : {lowest}")

print("\n")
print("-----------Question:21-------------")
#calculate Total, Highest and lowest in a single program using for loop.
numbers = [45, 12, 78, 34, 90, 23, 56]
highest=numbers[0]
for i in numbers:
    if i>highest:
        highest=i
print(f"Highest: {highest}")
lowest=numbers[0]
for i in numbers:
    if i<lowest:
        lowest=i
print(f"Lowest: {lowest}")
total=0
for i in numbers:
    total+=i
print(f"Total: {total}")

print("\n")
print("-----------Question:22-------------")
#Calculate average using for loop
#do not use sum() and len() function
marks = [78, 85, 92, 67, 74]
total_sum=0
count=0
for i in marks:
    total_sum+=i
    count+=1
print(f"Average Marks is: {total_sum/count} ")