#units of time

days= int(input("Enter the days: "))
hours= int(input("Enter the hours: "))
minutes= int(input("Enter the minutes: "))
seconds= int(input("Enter the seconds: "))

# converting days into seconds
days_in_sec = 86400 * days

#Converting hours into seconds
hours_in_sec = 3600 * hours

# converrting minutes into seconds
minutes_in_sec = 60 * minutes

# total time in seconds
total_time_in_seconds = days_in_sec + hours_in_sec + minutes_in_sec + seconds
print(f"Total time in seconds: {total_time_in_seconds}")
