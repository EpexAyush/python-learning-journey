print("-------------Question:23-------------")
#Student marks analysis
marks = [67, 89, 45, 92, 76, 81, 58]
total=0
for i in marks:
    total+=i
print(f"Total Marks: {total}")
highest=marks[0]
for i in marks:
    if i>highest:
        highest=i
print(f"Highest Marks: {highest}")
lowest=marks[0]
for i in marks:
    if i<lowest:
       lowest=i
print(f"Lowest Marks: {lowest}")
count=0
for i in marks:
    count+=1
print(f"Average Marks: {total/count}")
print("\n")

print("----------------Question:24---------------")
#Count positive, Neagtive and Zero
numbers_int=[12,-7,0,25,-14,8,0,-3,19]
#using for loop we have to count these numbers.
count_neg=0
for i in numbers_int:
    if i<0:
        count_neg+=1
print(f"Negative Numbers: {count_neg}")
count_pos=0
for i in numbers_int:
    if i>0:
        count_pos+=1
print(f"Positive Numbers: {count_pos}")
count_zeros=0
for i in numbers_int:
    if i==0:
        count_zeros+=1
print(f"Zeros: {count_zeros}")
print("\n")

print("--------------Question:25------------------")
#Count even and odd numbers using for loop
numbers = [12, 7, 24, 15, 8, 31, 42, 19, 50]
count_even=0
for i in numbers:
    if i%2==0:
        count_even+=1
print(f"Even Numbers: {count_even}")
count_odd=0
for i in numbers:
    if i%2!=0:
        count_odd+=1
print(f"Odd Numbers: {count_odd}")
print("\n")

print("---------------Question:26-----------------")
#sales analysis using for loop
sales = [1200, 850, 2300, 1750, 950, 3100, 1450]
total_sale=0
for i in sales:
    total_sale+=i
print(f"Total Sales: {total_sale}")
highest_sale=sales[0]
for i in sales:
    if i>highest_sale:
        highest_sale=i
print(f"Highest Sales: {highest_sale}")
lowest_sale=sales[0]
for i in sales:
    if i<lowest_sale:
        lowest_sale=i
print(f"Lowest sale: {lowest_sale}")
count_sale=0
for i in sales:
    count_sale+=1
print(f"Average Sales: {total_sale/count_sale}")
print("\n")

print("-------------Question:27------------------")
#Find Numbers Greater Than 50 using for loop.
number_greater = [23, 67, 45, 89, 12, 54, 31, 76, 48]
count_greater=0
for i in number_greater:
    if i>50:
        count_greater+=1
        print(i)
print(f"Numbers greater than 50 = {count_greater}")
print("\n")

print("---------------Question:28-----------------")
#Find Numbers Divisible by 3
numbers_div = [12, 17, 24, 31, 36, 41, 45, 52, 60]
count_div=0
print("Numbers divisible by 3:")
for i in numbers_div:
    if i%3==0:
        count_div+=1
        print(i)
print(f"Total Numbers: {count_div}")
print("\n")

print("----------------Question:29-----------------")
#Separate Even & Odd using for loops
num=[13, 24, 37, 42, 51, 68, 75, 80]
even_count=0
print("Even Numbers:")
for i in num:
    if i%2==0:
        even_count+=1
        print(i)
print(f"Even Count:{even_count}")
print("\n")
odd_count=0
print("Odd Numbers:")
for i in num:
    if i%2!=0:
        odd_count+=1
        print(i)
print(f"Odd count:{odd_count}")
print("\n")
print("-------------Question:30--------------------")
#Complete Number Analysis using for loop
com_number=[18, 45, 7, 92, 34, 61, 25, 80]

#find out the total sum
total_1=0
for i in com_number:
    total_1+=i
print(f"Total: {total_1}")

#find out the maximum number
maximum_num=com_number[0]
for i in com_number:
    if i>maximum_num:
        maximum_num=i
print(f"Highest: {maximum_num}")

#find out the minimum number
minimum_num=com_number[0]
for i in com_number:
    if i<minimum_num:
        minimum_num=i
print(f"Lowest: {minimum_num}")

#find out the average
count_com=0
for i in com_number:
    count_com+=1
print(f"Average: {total_1/count_com}")

#Even number count
even_num_count=0
for i in com_number:
    if i%2==0:
        even_num_count+=1
print(f"Even Count: {even_num_count}")

#odd number count
odd_num_count=0
for i in com_number:
    if i%2!=0:
        odd_num_count+=1
print(f"Odd count: {odd_num_count}")

#count of numbers which are greater than 50
count_50=0
for i in com_number:
    if i>50:
        count_50+=1
print(f"Number Greater Than 50: {count_50}")

