# Ideal Gas Law

pressure = int(input("Enter Pressure (in pascals): "))
volume= int(input("Enter Volume (in litres): "))
temp= int(input("Enter Temprature (in degree celcius): "))

#R is a universal gas constant which is
r= 8.314 # in J per mol per kelvin

# Convert litres to cubic metres
volume_m3 = volume / 1000

#Computing the moles of gas

temp_kelvin = (273.15 + temp)
moles_of_gas= (pressure*volume_m3)/(r*temp_kelvin)

print(f"moles of gas: {moles_of_gas:.2f}")