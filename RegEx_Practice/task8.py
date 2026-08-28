import re
message="Release 3.13; build 251; year 2011"
match_output=re.search("[0-9][0-9]",message)
print(f"First two-digit match: {match_output.group()} and {match_output.span()}")
match_wildcard=re.search("[0-9].[0-9]",message)
print(f"Wildcard match: {match_wildcard.group()} and {match_wildcard.span()}")
match_literal=re.search("[0-9][.][0-9][0-9]",message)
print(f"Literal-dot version: {match_literal.group()} and {match_literal.span()}")