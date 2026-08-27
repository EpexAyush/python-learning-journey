#-----------------------------Task:1--------------------------------

#creating a file named Sample.txt
'''open("Sample.txt","xt")'''

#writing content on sample.txt file
'''file_handler=open("Sample.txt","wt")
file_handler.write("This is a sample text file.\n")
file_handler.write("It contains multiple lines.")'''

#Actual task is starts from here.
import os
file_name_or_path="Sample.txt"

if os.path.exists(file_name_or_path):
    print("--------------File Exists--------------")
    print("Reading file content:")
    file_handler=open(file_name_or_path,"rt")
    print(f"Line 1: {file_handler.readline().rstrip()}")
    print(f"Line 2: {file_handler.readline()}")
    print("---------------------------------------")

else:
    print(f"Error: The file '{file_name_or_path}' was not found.")

#-----------------------------Task:2--------------------------------
user_input=input("Enter text to write to the file: ")
with open("output.txt","wt") as file_handler:
    file_handler.write(user_input)
    print("Data Successfully written to output.txt\n")
# -----------------------------------------------------

user_input_2=input("Enter additional text to append: ")
with open("output.txt","at") as file_handler:
    file_handler.write(F"\n{user_input_2}")
    print("Data successfully appended.\n")

#------------------------------------------------------

with open("output.txt","rt") as file_handler:
    print("Final content of output.txt:")
    print(file_handler.read())



