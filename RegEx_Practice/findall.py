import re
# .findall() ka use pattern ke saare matches find krne ke liye kiya jata hai aur results ko ek list ke form me return krta hai. 
phones = "A 9876543210, B 9123456789, C 1234567"
pattern=r"\d{10}"
all_matches=re.findall(pattern,phones)
print(f"Phone numbers: {all_matches}")


# ------------------------------------------------------

text= "Phones 9876543210 1234567 | version 3.13.5"
pattern_1=r"\d+"
pattern_2=r"\d{7,15}"
pattern_3=r"\d{7,}"
all_results_pat_1=re.findall(pattern_1,text)
all_results_pat_2= re.findall(pattern_2,text)
all_results_pat_3=re.findall(pattern_3,text)
print(f"Pattern 1: {all_results_pat_1}")
print(f"Pattern 2: {all_results_pat_2}")
print(f"Pattern 3: {all_results_pat_3}")

# --------------------------------------------------------


text="Valid 9876543210 Overlong 12345678901234567890"
pattern_1=r"\d{7,15}"
pattern_2=r"\d{7,15}\b"
pattern_3=r"\b\d{7,15}\b"
all_results_pat_1=re.findall(pattern_1,text)
all_results_pat_2=re.findall(pattern_2,text)
all_results_pat_3=re.findall(pattern_3,text)
print(f"Pattern 1: {all_results_pat_1}")
print(f"Pattern 2: {all_results_pat_2}")
print(f"Pattern 3: {all_results_pat_3}")

# -----------------------------------------------------