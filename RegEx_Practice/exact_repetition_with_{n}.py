import re

message="ID: 9 current Python"
pattern=r"[a-z]{4}"
match_object=re.search(pattern,message)
print(f"Match object 1: {match_object.group()} and span: {match_object.span()}")


#now we are matching one uppercase letter followed by exactly 5 lowercase letters
message="The best tool is Python today."
pattern=r"[A-Z][a-z]{5}"
match_object=re.search(pattern,message)
print(f"Match object 2: {match_object.group()} and span: {match_object.span()}")


#we are finding the exactly three consecutive digits
message="Room 7, code 251, ref 88"
pattern=r"[0-9]{3}"
match_object=re.search(pattern,message)
print(f"Match object 3: {match_object.group()} and span: {match_object.span()}")


#find a pattern in which exactly five time word characters repeats
#word character "\w" it matches the letters,digits and underscore
message="##ab_12!!"
pattern=r"\w{5}"
match_object=re.search(pattern,message)
print(f"Match object 4: {match_object.group()} and span: {match_object.span()}")


#repeat whitespaces (general space,\t,\n) exactly two times
#here i have used repr function so that spaces will cleary visible
message="alpha  beta"
pattern=r"\s{2}"
match_object=re.search(pattern,message)
print(f"Match object 5: {repr(match_object.group())} and span: {match_object.span()}")
