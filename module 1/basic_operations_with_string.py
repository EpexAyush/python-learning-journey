#========================================
#Challenge 1: Data Extraction(Slicing) 
#========================================
date_string="2026-08-15"

#hume date_strings me year ko extract karna hai
print("--------Challenge 1 Output---------")
print(f"Year: {date_string[0:4]}")

print("\n")

# ==========================================
# Challenge 2: Form Cleaning & F-strings
# ==========================================
raw_input="    aMaN kUmAr  "
# Task1: Aage piche ke sapce remove krne hai and har word ka pehla letter capital krna hai
print("-------Challenge 2 Outputs------")
print(f"1: {raw_input.strip().title()}")
#Task2: Welcome, Aman Kumar print karna hai 
print(f"2: Welcome, {raw_input.strip().title()}")

print('\n')

#===================================================
#Challenge 3: The Spam Filter (Membership & Count)
#===================================================
subject = "URGENT! You won a LOTTERY!!!"

# Task 1: Subject ko lower case mein convert karein.
# Task 2: Check karein ki 'urgent' word usme hai ya nahi (True/False).
# Task 3: Count karein ki '!' symbol kitni baar aaya hai.

print("-------Challenge 3 Outputs--------")
print(f"1: {subject.lower()}")
print(f"2: {"URGENT" in subject}")
print(f"3: ! mark comes {subject.count("!")} times.")

print("\n")

# ==========================================
# Challenge 4: File Extension Validator
# ==========================================
filename = "profile_pic.PNG"

# Task: Code likhein jo check kare ki filename '.png' ya '.jpg' par end hota hai (Hint: pehle filename ko lower case karna mat bhulna).

print("---------Challenge 4 Output---------")
filename= filename.lower()
is_valid= filename.endswith(".png") or filename.endswith(".jpg")
print(f"Is Filename ended with .png or .jpg ? Ans is {is_valid}")