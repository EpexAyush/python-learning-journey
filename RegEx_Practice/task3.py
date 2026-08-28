import re
message="Room 7, code 251, floor 8"
print(f"Two digits: {re.search("[0-9][0-9]",message).group()}")
print(f"Three digits: {re.search("[0-9][0-9][0-9]",message).group()}")