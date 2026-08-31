# * quantifier zero or more repetitions ko batata hai.
# * ka matlab hai ki previous element optional hai aur wo 0 se lekar jitni baar bhi repeat ho sakta hai.


import re


#Uppercase letter followed by zero or more lowercase letters.
message="X Python"
pattern=r"[A-Z][a-z]*"
match_object=re.search(pattern,message)
print(f"Matched output 1: {match_object.group()} and span: {match_object.span()}")


#Allow any number of spaceS after 1 uppercase letter.
# \s shorthand class se hum whitespaces find out krte hai.
# we are using repr() function so that hume spaces feel ho.
message="A                B"
pattern=r"[A-Z]\s*"
match_object=re.search(pattern,message)
print(f"Matched output 2: {repr(match_object.group())} and span: {match_object.span()}")


#