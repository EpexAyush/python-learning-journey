import math
#radius in meters
radius=int(input("Enter radius(m): "))

#computing the area of the circle
area_of_circle=math.pi*(radius**2)
print(f"1. Area of the circle is: {area_of_circle:.2f}")

#computing the volume of the sphere
volume_of_sphere=(4/3)*(math.pi*(radius**3))
print(f"2. Volume of the sphere is: {volume_of_sphere:.2f}")