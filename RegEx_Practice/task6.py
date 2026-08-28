import re

message="House number: 251/A"

#here "." is representing any chracter like: number, text, special character except new line(\n)
matched_text=re.search("[0-9].[0-9]",message)
print(f"Wildcard match: {matched_text.group()}")
print(f"Character matched by .: {matched_text.group()[1]}")

message2="1\n2"
print(f"Across newline: {re.search("[0-9].[0-9]",message2)}")