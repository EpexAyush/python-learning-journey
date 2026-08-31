""" + Quantifier ka matlab ki isse pehle aane wala element kam se kam 1 baar repeat hua ho
aur maximum kitni bhi baar aaya ho.
"""
import re

#match an uppercase-started word
message="The current Python version"
pattern=r"[A-Z][a-z]+"
mathched_object=re.search(pattern,message)
print(f"Matched Output 1: {mathched_object.group()} and span: {mathched_object.span()}")

#Find the first run of one or more digits.
message="Version x3.13 and build 251"
pattern=r"\d+"
mathched_object=re.search(pattern,message)
print(f"Matched object 2: {mathched_object.group()} and span: {mathched_object.span()}")

# Match one or more spaces
message="one                 two"
pattern=r"\s+"  # \s whitespace shorthand class
mathched_object=re.search(pattern,message)
print(f'''Match output 3: {repr(mathched_object.group())}
length of matched output: {len(mathched_object.group())} and message length= {len(message)}
span: {mathched_object.span()}''')

#Match one or more word character
message="###abc_123!!!"
pattern=r"\w+"
mathched_object=re.search(pattern,message)
print(f"Matched object 4: {mathched_object.group()} and span: {mathched_object.span()} ")

