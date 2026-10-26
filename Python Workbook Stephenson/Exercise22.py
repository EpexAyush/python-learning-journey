# Area of the Triangle

import math

s1= float(input("Enter the length of side 1 (m): "))
s2= float(input("Enter the length of side 2 (m): "))
s3= float(input("Enter the length of side 3 (m): "))

# calculating the S = (S1 + S2 + S3)/2
s= (s1 + s2 + s3)/2

# computing the area of the triangle

area= math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

print(f"The area of the triangle: {area:.2f} sq. meters")