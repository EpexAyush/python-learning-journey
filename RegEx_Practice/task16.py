# Mini Regex Inspection Report

import re
text= "ID A-5 note Bx7 end"
pattern_1=r"[A-Z].[0-9]"
# here "." is representing any character,numbers except only new line (\n)
print(f"Pattern 1 First Match: {re.search(pattern_1,text).group()} and span: {re.search(pattern_1,text).span()}")

pattern_2=r"[A-Z][a-z]\d"
# here "\d" represents any digits from 0 to 9.
print(f"Pattern 2 First Match: {re.search(pattern_2,text).group()} and span: {re.search(pattern_2,text).span()}")

pattern_3=r"[A-Z][a-z]\s"
# here "\s" matches white space characters like \n,\t or general space.
print(f"Pattern 3 First Match: {re.search(pattern_3,text) }")