print("-------------Queston:1------------")
#Write a Python program to create a list of marks of 10 students and perform the following operations:
marks = [78, 65, 89, 92, 65, 74, 81, 90, 65, 88]
#1: Adding a new mark using append() function
marks.append(99)
print(f"1. Added a 99 Mark in the Marks list: {marks}")

#2:Adding multiple marks using extend() function:
marks.extend([55,88,33,88])
print(f"2. Adding multiple marks: {marks}")

#3:Insert a mark at a specific position using insert()
marks.insert(2,100)
print(f"3. Added 100 marks at the 2nd index/position: {marks}")\

#4:Remove a particular mark using remove()
marks.remove(100)
print(f"4. Removed 100 mark from the list: {marks}")

#5:Remove the last mark using pop()
marks.pop()
print(f"5. Removed last mark 88 using pop(): {marks}")

#6:Find the position of a mark using index()
print(f"6. Index/position of 99 mark in the list: {marks.index(99)}")

#7:Count how many students obtained a particular mark using count()
print(f"7. 88 mark obtained by students: {marks.count(88)}")

#8:Sort the marks in ascending order using sort()
marks.sort()
print(f"8. List in the ascending order: {marks}")

#9:Reverse the list using reverse()
marks.reverse()
print(f"9. Reverse order of the list: {marks}")

#10:Create a copy of the list using copy()
import copy
marks_copy=copy.copy(marks)
print(f"10. Created a copy of a marks list: {marks_copy}")

print("--------------------------------------------------------------\n")

print("-------------Queston:2------------")
#Shopping Cart Management
product_list=["Shampoo","Face Wash","Maggie","Watch","Mouse Pad","Diary","Nescafe Cold Coffee"]

#1:Add a new product using append().
product_list.append("Nike Shoes")
print(f"1. Added Nike Shoes in the list using append(): {product_list}")

#2:Add several products using extend()
product_list.extend(["Earings","Necklace","Bracelet"])
print(f"2. Added 3 items in the list using extend(): {product_list}")

#3:Insert a product at a particular position using insert()
product_list.insert(5,"Black Jeans")
print(f"3. Added black jeans at the 5th index using insert(): {product_list}")

#4:Remove a product using remove()
product_list.remove("Earings")
print(f"4. Removed Earings from the list using remove(): {product_list}")

#5:Remove an item using pop()
product_list.pop(-3)
print(f"5. Removed an item from the last 3rd index using pop(): {product_list}")

#6:Display the number of times a particular product occurs using count().
print(f"6. How many times Maggie comes in the list: {product_list.count("Maggie")}")

#7:Find the position of a product using index().
print(f"7. Finding Maggie position in the list using index(): {product_list.index("Maggie")}")

#8:Sort the products alphabetically using sort().
product_list.sort()
print(f"8. Sorting the list in the A-Z order using sort(): {product_list}")

#9:Reverse the product list using reverse().
product_list.reverse()
print(f"9. Sorting the list in the Z-A order using reverse(): {product_list}")

#10:Create a backup of the cart using copy().
import copy
copy_prod_list= copy.copy(product_list)
print(f"10. Copied product list: {copy_prod_list}")

#11:Clear the original cart using clear()
product_list.clear()
print(f"11. Cleared all the products from the list using clear(): {product_list}")
print("--------------------------------------------------------------\n")

print("-------------Queston:3------------")
#Employee Salary Processing
salary = [25000, 32000, 28000, 45000, 32000, 50000, 28000]

#1:Adding a new salary
salary.append(128823)
print(f"1. Added a new salary: {salary}")

#2:Add salaries of newly joined employees.
new_emp_salary=[55000,67000,254000]
salary.extend(new_emp_salary)
print(f"2. Added new employees salaries: {new_emp_salary}")

#3:Insert a salary at position 3
salary.insert(3,23299)
print(f"3. Inserted a salary at the index 3: {salary}")

#4:Remove a salary
salary.remove(28000)
print(f"4. Removed 28000 salary from the list: {salary}")

#5:Remove the last salary
salary.pop()
print(f"5. Removed last salary from the list: {salary}")

#6:Find the position of salary 32000.
print(f"6. Position of 32000 in the list: {salary.index(32000)}")

#7:Count how many employees receive 28000 salary
print(f"7. There are {salary.count(28000)} person receiving 28000 salary.")

#8:Sort salaries from lowest to highest
salary.sort()
print(f"8. Sorting salary in the ascending order: {salary}")

#9:Reverse the sorted salary list
salary.reverse()
print(f"9. Sorting salary in the descending order: {salary}")

#10:Make a copy of the salary list
import copy
copy_salary=copy.copy(salary)
print(f"10. Copy file of salary: {copy_salary}")

#11:Display the Highest and Lowest salary using appropiate list operations
print(f"11. Highest salary is {max(salary)} and lowest salary is {min(salary)}")
print("--------------------------------------------------------------\n")

print("-------------Queston:4------------")
#Unique Number Generator
numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60, 10]

#1:We are checking that which number how many times are repeated.
print("1. Checking how many times list number is repeating:")
for i in range(10,61,10):
    print(f"number {i} repeated {numbers.count(i)}")

#2:Use append() to create the unique list.
numbers.append(88)
print(f"2. Unique list created using append(): {numbers}")

#3:Use sort() to arrange the unique values.
numbers.sort()
print(f"3. Sorted order of the numbers: {numbers}")

#4:Use reverse() to display them in descending order
numbers.reverse()
print(f"4. Reverse Order: {numbers}")

#5:Use index() to find the position of a user-entered number
user_input=int(input("Enter a number to find index: "))
print(f"\033[1A\033[2K\r5. Index of {user_input} is {numbers.index(user_input)} ")

#6:Use copy() to create a duplicate of the final list.
import copy
copy_numbers_list= copy.copy(numbers)
print(f"6. Copied List of numbers: {copy_numbers_list}")