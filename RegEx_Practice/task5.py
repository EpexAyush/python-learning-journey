import re
message="Code 47"
result=re.search("13",message)
if result:
    print("13 in message: True")
else:
    print("13 in message: False")


print(f"find(\"13\"): {message.find("13")}")
print(f"Index(\"47\"): {message.index("47")}")

match_value=re.search("[0-9][0-9]",message).group()
print(f"Regex two-digit match: {match_value}")
