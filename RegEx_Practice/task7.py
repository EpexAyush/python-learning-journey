import re
version_message= "The current Python version is 3.13."
year_message="This year is 2011"
print(f"Version match: {re.search("[0-9][.][0-9][0-9]",version_message).group()}")
print(f"Year match: {re.search("[0-9][.][0-9][0-9]",year_message)}")