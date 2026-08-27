#os.path.exist()
# pathlib.Path.exists() 
#the exist() function is the part of the os module.
#it is the straight forward technique to check a file exist or not.

import os

file_name=r"C:\Users\legen\OneDrive\Desktop\python-learning-journey\Experiment_2.txt"
print("---------------------------------------------------------------")
if os.path.exists(file_name):
    print(f"This file ({file_name}) exist in your database.")
else:
    print(f"This file ({file_name}) does not exist in your database.")
print("---------------------------------------------------------------")
print("\n")
from pathlib import Path
file_path= Path("Experiment_3.txt")
print("---------------------------------------------------------------")
if file_path.exists():
    print(f"File {file_path} Exist.")
else:
    print(f"File {file_path} does not exist.")
print("---------------------------------------------------------------")
