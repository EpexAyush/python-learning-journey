import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
#calculations
sum=a+b
diff=a-b
prod=a*b
div=a/b
rem=a%b
log_cal=math.log10(a)
expo=a**b
print("\n-------Output-------")
print(f"The sum of a and b: {sum}")
print(f"The difference when b is substracted from a: {diff}")
print(f"The product of a and b: {prod}")
print(f"The quotient when a is divided by b: {div}")
print(f"The remainder when a is divided by b: {rem}")
print(f"The result of log10(a): {log_cal}")
print(f"The result of a^b: {expo}")
