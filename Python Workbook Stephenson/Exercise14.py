height_in_feet=int(input("Enter height in feet: "))
height_in_inch=int(input("Enter height in inch: "))

#computation of heights
one_foot_in_inch=12
one_inch_in_cm=2.54

height_in_cm=(height_in_feet*one_foot_in_inch+height_in_inch)*one_inch_in_cm
print(f"{height_in_feet} feet {height_in_inch} inches in cm is: {height_in_cm}")