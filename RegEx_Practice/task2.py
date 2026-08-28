import re
message="House number: 251/A"
range_match=re.search("[0-9][0-9]",message)
print(range_match)
print(f"Range match: {range_match.group()}")
print(f"Range span: {range_match.span()}")

explicit_match=re.search("[0123456789][0123456789]",message)
print(f"Explicit-set match: {explicit_match.group()}")
print(f"Explicit-set span: {explicit_match.span()}")