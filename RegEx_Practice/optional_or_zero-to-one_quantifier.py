# ? quantifier ka matlab hai ki iske just pehle wala character/group 0 ya 1 baar aa sakta hai. Yaani woh optional hai.

import re

#Optional lowercase letter after an uppercase letter
message="The Python Course"
pattern=r"[A-Z][a-z]?"
matched_object=re.search(pattern,message)
print(f"Match output 1: {matched_object.group()} and span: {matched_object.span()}")


#Optional digits
message="code A7, then B"
pattern=r"[A-Z]\d?"
matched_object=re.search(pattern,message)
print(f"Matched output: {matched_object.group()} and span: {matched_object.span()}")


#Optional single space between two uppercase letters
message="AB A B"
pattern=r"[A-Z]\s?[A-Z]"
matched_object=re.search(pattern,message)
print(f"Matched output 3: {repr(matched_object.group())} and span: {matched_object.span()}")
