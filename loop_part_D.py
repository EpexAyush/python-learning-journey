print("-----------Question:15-------------")
student = {
    "name": "Ayush",
    "age": 23,
    "course": "CSDA",
    "semester": 1
}
for keys in student:
    print(keys) #we have printed the keys here for the above dictonary.

print("\n")

print("-----------Question:16-------------")
student = {
    "name": "Ayush",
    "age": 23,
    "course": "CSDA",
    "semester": 1
}
#now we have to print the values in the output
for value in student:
    print(student.get(value))

print("\n")

print("-----------Question:17-------------")
marks = {
    "Physics": 78,
    "Chemistry": 85,
    "Maths": 92,
    "English": 74
}
#we have to show output same as key-value pairs using for loop.
for key_value_pair in marks:
    print(key_value_pair,":",marks.get(key_value_pair))