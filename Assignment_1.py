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
if user_input in numbers:
    print(f"\033[1A\033[2K\r5. Index of {user_input} is {numbers.index(user_input)} ")
else:
    print("\033[1A\033[2K\r5. This number is not present in the list.")

#6:Use copy() to create a duplicate of the final list.
import copy
copy_numbers_list= copy.copy(numbers)
print(f"6. Copied List of numbers: {copy_numbers_list}")

#7:clear the list using clear()
numbers.clear()
print(f"7. cleared list: {numbers}")
print("--------------------------------------------------------------\n")

print("-------------Queston:5A------------")
#Student Result Analysis
marks_student = [56, 78, 90, 45, 67, 78, 89, 92, 56, 78]
marks_student.extend([67,89])
print(f"1. Added 67,89 marks of two new students: {marks_student}")
marks_student.insert(3,99)
print(f"2. Inserted 99 marks at the 3rd index: {marks_student}")
marks_student.remove(56)
print(f"3. Removed 56 mark from the list: {marks_student}")
marks_student.pop()
print(f"4. Removed last mark from the list: {marks_student}")
print(f"5. Students who scored 78: {marks_student.count(78)}")
print(f"6. Index of the first 90 mark is: {marks_student.index(90)}")
marks_student.sort()
print(f"7. Marks in the ascending order: {marks_student}")
marks_student.reverse()
print(f"8. Reverse the order of the marks list: {marks_student}")
student_marks_copy=copy.copy(marks_student)
print(f"9. Copied file of student marks: {student_marks_copy}")
print(f"10. Maximum marks is {max(marks_student)} and Minimum marks is {min(marks_student)}")
print("--------------------------------------------------------------\n")

print("-------------Queston:5B------------")
#Student Marks Tuple Analysis
marks_tup = (78, 65, 89, 92, 65, 74, 81, 90, 65, 88)
print(f"1. Length of the marks tuple: {len(marks_tup)}")
print(f"2. How many students scored 65 marks: {marks_tup.count(65)}")
print(f"3. Position of 92 in the tuple is: {marks_tup.index(92)}")
print(f"4. The highest marks is {max(marks_tup)} and Lowest marks is {min(marks_tup)}")
print(f"5. Sum of all the marks: {sum(marks_tup)}")
print(f"6. Average marks: {sum(marks_tup)/len(marks_tup)}")
sorted_tuple=tuple(sorted(marks_tup))
print(f"7. Sort the tuple in the Ascending Order: {sorted_tuple}")
reversed_tuple=marks_tup[::-1]
print(f"8. Reversed Order of the tuple using slicing: {reversed_tuple} ")
print("--------------------------------------------------------------\n")

print("-------------Queston:5C------------")
# Employee ID Tuple
employee_ids = (101, 105, 103, 101, 108, 110, 105, 115)
print(f"1. Total Employees: {len(set(employee_ids))}")
print(f"2. How many times ID 101 occurs: {employee_ids.count(101)}")
print(f"3. Position of ID 108: {employee_ids.index(108)}")
user_input=int(input("4. Enter a Emp ID: "))
if user_input in employee_ids:
    print(f"\033[1A\033[2K\r4. Yes!, Emp ID present in our Database. ")
else:
    print("\033[1A\033[2K\r4. Emp ID not found in Database.")
print(f"5. Smallest Emp ID is {min(employee_ids)} and Largest Emp ID is {max(employee_ids)}")
sorted_emp_id= tuple(sorted(employee_ids))
print(f"6. Sorted Emp IDs: {sorted_emp_id}")
reversed_emp_ids= tuple(reversed(employee_ids))
print(f"7. Reverse Order of Emp IDs: {reversed_emp_ids}")
print("--------------------------------------------------------------\n")

print("-------------Queston:5D------------")
# Product Price Tuple
prices = (450, 1200, 750, 450, 999, 1500, 750, 2000)
print(f"1. Total Price: {sum(prices)}")
print(f"2. Average Price: {sum(prices)/len(prices)}")
print(f"3. Minimum price is {min(prices)} and Maximum price is {max(prices)}")
print(f"4. How many Products cost 450: {prices.count(450)}")
print(f"5. position of the first product costing 750: {prices.index(750)}")
sorted_prices= tuple(sorted(prices))
print(f"6. Sorted Order: {sorted_prices}")
desc_prices=tuple(sorted(prices,reverse=True))
print(f"7. Descending Order: {desc_prices}")
print(f"8. First Three Prices Using Slicing: {prices[0:3]}")
print(f"9. Last three prices using slicing: {prices[-1:-4:-1]}")
print("--------------------------------------------------------------\n")

print("-------------Queston:5D------------")
#Subject Tuple Processing
subjects = ("Python", "Java", "C++", "Python","DBMS", "Java", "AI", "Python")

#1:Display total number of the subjects
print(f"1. Total number of subjects: {len(set(subjects))}")

#2:Count the occurrence of "Python"
print(f"2. How many times 'Python' Comes: {subjects.count("Python")}")

#3:Find the first position of "Java"
print(f"3. Index of 'JAVA': {subjects.index("Java")}")

#4:Check whether "AI" exists.
print(f"4. Is AI exist in the tuple?: {"AI" in subjects}")

#5:Display the tuple in reverse order
rever_sub=tuple(reversed(subjects))
print(f"5. Reversed Ordedr of the tuple: {subjects}")

#6:Display the Subjects from index 2 to 6.
print(f"6. Subjects from index 2 to 6: {subjects[2:7]}")

#7:Convert Tuple into List
new_list_tuple=list(subjects)
print(f"7. Tuple {subjects} converted into List {new_list_tuple}")

#8:Add a new subject to the list
new_list_tuple.append("English")
print(f"8. Added English in the list: {new_list_tuple}")

#9:Conveted a list back into the tuple:
updated_tuple=tuple(new_list_tuple)
print(f"9. Now the updated tuple is: {updated_tuple}")
print("--------------------------------------------------------------\n")

print("-------------Queston:5E------------")
#Tuple-Based Sales Analysis
sales = (25000, 32000, 28000, 45000, 32000,50000, 28000, 45000, 52000, 32000)
