# =============================
# Challenge 1: Age Calculator
# =============================
user_name=input("Enter Your Name: ")
user_birth_year=int(input("Enter Your Birth Year: "))
current_year=2026
print("---------Challenge 1-----------")
# We have to calculate the Age of the User according to current year 2026
print(f"{user_name} you are {current_year-user_birth_year} years old.")

print("\n")

#=============================================
# Challenge 2: The Bug Fixer (Fix the Error)
#=============================================
score = 95
# Is line mein error aayega, isko theek karke likhein:
# print("Aapka final score " + score + " hai!") 

print("-------Challenge 2----------")
print("Aapka final Score "+str(score)+" hai!")

print('\n')

print("========================================")
print("Challenge 3: E-Commerce Bill Calculator")
print("========================================")

# Task 1: price ko input lein aur float mein convert karein.
item_price=float(input("Enter Your Item Price: "))

# Task 2: quantity ko input lein aur int mein convert karein.
item_quantity=int(input("Enter Item Quantity: "))
print("\n")
print("--------Challenge 3 Output---------------")
# Task 3: Total bill (price * quantity) nikal kar print karein.
total_bill=(item_price*item_quantity)
print(f"Your Total Bill is: {total_bill}")

print("\n")

print("=========================================================================================")
print("Challenge 4: The Logic Gates (Boolean Conversion)")
print("=========================================================================================")
username1="admin"
username2=""
print("----------------------------------challenge 4 Output--------------------------------------")
print(f"username1 will give {bool(username1)} and username2 will give {bool(username2)}.")