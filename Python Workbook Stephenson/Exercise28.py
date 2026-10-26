temp_air = float(input("Enter the temprature of the air (degree C): "))
wind_speed = float(input("Enter the wind speed (km per hour): "))


wci= 13.12 + (0.6215*temp_air) - (11.37 *(wind_speed**0.16)) + (0.3965*temp_air* (wind_speed**0.16))

print(f"Wind chill index: {round(wci)}")