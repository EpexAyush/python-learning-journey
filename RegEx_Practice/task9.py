#How a normal python string and a raw string treat backslash sequences differently.
normal_text="A\nB"
raw_text=r"A\nB"
print("-------------------------------")
print(f"Normal Text: {repr(normal_text)}")
print(f"Raw Text: {repr(raw_text)}")
print(f"Normal Length: {len(normal_text)}")
print(f"Raw Length: {len(raw_text)}")
print("-------------------------------")