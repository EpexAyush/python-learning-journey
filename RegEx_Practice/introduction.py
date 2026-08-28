import re

user_input=input("Enter Data: ")

output=re.search("[0-9][0-9]",user_input)
if output:
    print(f"Two-digit pattern: {output.group()}")
else:
    print("Two-digit pattern found: No match found.")

output_2 = re.search("[0-9][0-9][0-9]", user_input)
if output_2:
    print(f"Three-digit pattern found: {output_2.group()}")
else:
    print(f"Three-digit pattern found: No match found.")

print("-----------------Task:2----------------------------\n")

Student_id= "Student ID: A23B, Room: 251, Batch: 2026, Code: X7Y9."
two_digit_num=re.search("[0-9][0-9]",Student_id)
if two_digit_num:
    print(f"Two-digit pattern: {two_digit_num.group()}")
else:
    print(F"Two-digit pattern: No match found.")


three_digit_num=re.search("[0-9][0-9][0-9]",Student_id)
if three_digit_num:
    print(f"Three-digit pattern: {three_digit_num.group()}")
else:
    print(F"Three-digit pattern: {three_digit_num}")

char_num_data=re.search("[0-9][A-Z]",Student_id)
if char_num_data:
    print(f"one digit and one character pattern: {char_num_data.group()}")
else:
    print(f"one digit and one character pattern: Match not found.")

con_char_data=re.search("[a-z][A-Z]",Student_id)
if con_char_data:
    print(f"one small and one big character pattern: {con_char_data.group()}")
else:
    print(f"one small and one big character pattern: Match not found.")

con_char_data_2=re.search("[a-z][a-z]",Student_id)
if con_char_data_2:
    print(f"both small character pattern: {con_char_data_2.group()}")
else:
    print(f"both small character pattern: Match not found.")

con_char_data_3=re.search("[A-Z][A-Z]",Student_id)
if con_char_data_3:
    print(f"both capital character pattern: {con_char_data_3.group()}")
else:
    print(f"both capital character pattern: Match not found.")



