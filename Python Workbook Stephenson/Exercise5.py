container_1=int(input("Enter number of containers holding 1 liter or less: "))
container_2=int(input("Enter number of containers holding more than 1 liter: "))

Total=(container_1*0.10)+(container_2*0.25)
print(f"Total refund is ${Total:.2f}")