distance=float(input("Enter distance in feet: "))

#conversions
one_foot_in_inch=12
one_yard_in_feet=3
one_mile_in_feet=5280

distance_in_inches= distance*one_foot_in_inch
distance_in_yards= distance/one_yard_in_feet
distance_in_miles=distance/one_mile_in_feet

print(f"1. Distance in inches: {distance_in_inches:.2f}")
print(f"2. Distance in yards: {distance_in_yards:.2f}")
print(f"3. Distance in miles: {distance_in_miles:.2f}")
