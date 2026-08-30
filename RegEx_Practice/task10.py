#Practice [A-Z], [a-z], case sensitivity, re.search(), matched text, span, and None.
#importing re module
import re

text_1= "code Camp starts Today"
pattern= r"[A-Z][a-z][a-z]"
m=re.search(pattern,text_1)
print(f"Match: {m.group()}")
print(f"Span: {m.span()}")

text_2="code camp starts today"
print(f"Second Search: {re.search(pattern,text_2)}")