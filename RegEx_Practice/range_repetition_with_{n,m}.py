#first uppercase letter and lowercase letter (minimum range=2 and maximum range=5)
import re
message="The Python Regex Course"
pattern=r"[A-Z][a-z]{2,5}"
match_object= re.search(pattern,message)
print(f"Matched object 1: {match_object.group()} and span: {match_object.span()}")


#match first consective digits which has a max and min range is 2,4

message="x7 y42 z12345"
pattern=r"\d{2,4}"
match_object=re.search(pattern,message)
print(f"Matched object 2: {match_object.group()} and span: {match_object.span()}")


#Match 3 to 6 word characters.
#\w word character and matches underscore,letters and digits only.
message="!!ab abc_12 xyz!!"
pattern=r"\w{3,6}"
match_object=re.search(pattern,message)
print(f"Matched object 3: {match_object.group()} and {match_object.span()}")


#find out the pattern match output of first 2 uppercase letters and 2 to 3 digits.
message="Bad X7, valid AB123, next ZX99"
pattern=r"[A-Z]{2}\d{2,3}"
match_object=re.search(pattern,message)
print(f"Matched object 4: {match_object.group()} and span: {match_object.span()}")


#comparing two patterns from each other
message="The current Python version is 3.13"
pattern_1=r"[A-Z][a-z]{5}"
pattern_2=r"[A-Z][a-z]{2,5}"

match_object_1=re.search(pattern_1,message)
match_object_2=re.search(pattern_2,message)

print(f" Matched output according to the pattern 1 is {match_object_1.group()} and according to the pattern 2 is {match_object_2.group()}")

#in the above comparison the result changes because we have changed the range, in the first pattern we have find one uppercase and 5 continous lowercase letters so the first match of this pattern will be "Python" and in the second pattern we have given a range from 2 to 5 means after 1 uppercase letter there are minimum 2 and maximum 5 lowercase letters arrive continously 