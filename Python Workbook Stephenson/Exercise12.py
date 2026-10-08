import math

lat_1=math.radians(float(input("Enter latitude of point 1: ")))
long_1=math.radians(float(input("Enter longitude of point 1: ")))
print("---------------------------------------------------------\n")
lat_2=math.radians(float(input("Enter latitude of point 2: ")))
long_2=math.radians(float(input("Enter longitude of point 2: ")))

#calculation of distance from point 2 to point 1
earth_radius=6371.01 #unit is in km.
distance=earth_radius*math.acos(math.sin(lat_1)*math.sin(lat_2)+math.cos(lat_1)*math.cos(lat_2)*math.cos(long_1-long_2))

print(f"The distance between the point 1 and point 2 is {distance} km")




