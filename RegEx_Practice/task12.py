#Prove that \s can match an ordinary space, \n, and \t, and remember that each is one character
import re

string= [("cat dog",r"[a-z][a-z][a-z]\s"),
        ("bird\nfish", r"[a-z][a-z][a-z][a-z]\s"),
        ("owl\tfox", r"[a-z][a-z][a-z]\s") 
        ]

for text,pattern in string:
    m=re.search(pattern,text)
    print(f"Repr Text according to the pattern: {repr(m.group())} & Span: {m.span()} ")
print("-------------------------------------------------")

for text,pattern in string:
    m=re.search(pattern,text)
    print(f"matched text: {m.group()} & span: {m.span()}")