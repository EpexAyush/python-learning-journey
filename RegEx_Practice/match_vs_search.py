import re

# .match() index 0 se pattern find krta hai
s1= "we are learning regex in Python."
pattern= r"[a-z]{2}"
match_result=re.match(pattern,s1)
print(f"Output 1: {match_result.group()}")

pattern=r"[a-z]{3}"
match_result=re.match(pattern,s1)
print(f"Output 2: {match_result}")

# .search() function index 0 se nhi pattern find out krta pure string me agar khi se bhi sabse pehle pattern mil jata hai to use capture kr leta hai.
pattern= r"[a-z]{3}"
match_result=re.search(pattern,s1)
print(f"Output 3: {match_result.group()}")