import math

radius=float(input("Enter the radius(m): "))
height=float(input("Enter the height(m): "))

#compute the volume of the cyclinder
#volume=base_area*height

base_area=math.pi*(radius**2)
volume=base_area*height

print(f"The Volume of the cylinder: {volume:.2f} cube meters")