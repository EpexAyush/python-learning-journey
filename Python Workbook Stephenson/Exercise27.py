height =  float(input("Enter the height(M): "))
weight = float(input("Enter the weight(KG): "))

bmi = weight/(height**2)

print(f"BMI: {bmi:.2f} kg/square meters")
