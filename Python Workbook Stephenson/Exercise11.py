user_input=float(input("Enter Fuel efficiency(MPG): "))

#conversion From MPG american units to Litre-per-100-km in canadian units
fuel_effi=235.3/user_input # canadian units 

print(f"The equivalent fuel efficiency in canadian units: {fuel_effi:.2F} Litre/100km")