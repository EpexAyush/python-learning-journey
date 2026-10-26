

# Exercise 25: Units of Time (Again)

seconds = int(input("Enter the number of seconds: "))

# Calculate days and remaining seconds
days = seconds // 86400
remaining = seconds % 86400

# Calculate hours and remaining seconds
hours = remaining // 3600
remaining = remaining % 3600

# Calculate minutes and remaining seconds
minutes = remaining // 60
seconds = remaining % 60

# Display time in D:HH:MM:SS format
print(f"Formatted time: {days}:{hours:02d}:{minutes:02d}:{seconds:02d}")
