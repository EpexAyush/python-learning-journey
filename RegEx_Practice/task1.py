import re
message="The current Python version is 3.13."
pattern="Python"
match_object=re.search(pattern,message)
print(match_object)
print(match_object.group())
print(match_object.span())
