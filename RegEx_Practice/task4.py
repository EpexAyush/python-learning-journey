import re
message="Codes: 13, 24, 57, 89"
match_object=re.search("[0-9][0-9]",message)

#only first matched digits will be printed remaining will not.
print(f"First match: {match_object.group()}")
print(f"Span: {match_object.span()}")
