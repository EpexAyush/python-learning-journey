# Compare \d and \D using the same string and observe how uppercase shorthand means the opposite
# class.
import re
text = "A9 Bx C#"
#\d matches any digit from 0 to 1.
pattern_1=r"[A-Z]\d"
print(f"Matched Text Pattern 1: {re.search(pattern_1,text).group()} and Span: {re.search(pattern_1,text).span()}")
#\D: matches any non digit characters other than 0 to 1.
pattern_2=r"[A-Z]\D"  
print(f"Matched Text Pattern 2: {re.search(pattern_2,text).group()} and Span: {re.search(pattern_2,text).span()}")