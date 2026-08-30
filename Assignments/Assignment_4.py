print("----------------TASK:1-------------------\n")

#Creating a  dictonary of student marks of class 10th:
student_marks={"Ayush":523,"Aman":500,"Ananya":560,"Anushka":540}
user_input=input("Enter a student name: ").capitalize()

if user_input in student_marks.keys():
    print(f"{user_input}'s marks: {student_marks[user_input]}")
else:
    print("Student not found.")


print("\n----------------TASK:2-------------------\n")

num_list=[1,2,3,4,5,6,7,8,9,10]
print(f"Original List: {num_list}")

#extracting the first five numbers from the list.
first_five_num = num_list[0:5]
print(f"Extracted first five elements: {first_five_num}")

#Reversing the extracted numbers list.
rev_ext_num_list = first_five_num.reverse()
print(f"Reverse extracted elements: {first_five_num}")