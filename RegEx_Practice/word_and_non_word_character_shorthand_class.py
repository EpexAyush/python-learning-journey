# Demonstrate the difference between \w and \W, including underscore and punctuation.

#\w: ye letter, digits and underscore ko match krta hai.
#\W: ye letter, digits and undedrscore ke alawa sab kuch match krta hai.

import re
text=  "ab_ cd# ef9"

pattern_1=r"[a-z][a-z]\w"
print(f"Matched Pattern 1: {re.search(pattern_1,text).group()}")

pattern_2=r"[a-z][a-z]\W"
print(f"Matched pattern 2: {re.search(pattern_2,text).group()}")

#matching pattern 1 in "ef9"
print(f"Pattern matched?: {re.search(pattern_1,"ef9").group() in text}  and output: {repr(re.search(pattern_1,"ef9").group())} and Span: {re.search(pattern_1,"ef9").span()}")