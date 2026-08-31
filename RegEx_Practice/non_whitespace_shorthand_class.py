#Use \S to require a character that is not whitespace(\n,\t,space) inke alawa sab kuch match krta hai digits numbers and special characters also.
import re

text= "Sun sky"
pattern=r"[a-z][a-z]\S"
matched_text=re.search(pattern,text)
print(f"Matched Text: {matched_text.group()}")
print(f"Span: {matched_text.span()}")