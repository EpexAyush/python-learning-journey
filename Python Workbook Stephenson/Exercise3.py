'''Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.'''


print("--------Area of a Room-------")
width=float(input("Enter Width(m): "))
length=float(input("Enter Length(m): "))

#calculating the area of a room
area=(length*width)
print(f"Area of your room is {area} square meters.")