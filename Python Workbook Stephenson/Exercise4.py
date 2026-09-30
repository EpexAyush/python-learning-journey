# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

lenght=float(input("Enter length in feet: "))
width=float(input("Enter width in feet: "))

#calculation
Area_in_acre=(lenght*width)/43560

print(f"The area of the field is {Area_in_acre:.2f} acres.")