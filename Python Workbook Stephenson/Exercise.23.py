# Area of a regular polygon

import math

total_sides = int(input("Enter the total number of side: "))
side_length = float(input("Enter the length of the side (m): "))

#computing the area of the polygon

area_of_polygon = (total_sides * (side_length)**2)/ (4 * math.tan(math.pi/total_sides))
print(f"Area of the polygon: {area_of_polygon:.2f} square meters.")