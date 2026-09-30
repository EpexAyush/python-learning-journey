cents_num=int(input("Enter a number of cents: "))

#Distributions of the cents
toonie=cents_num//200 # 1 toonie value is 200 cents
loonie=(cents_num%200)//100 #value of 1 loonie is 100 cents
quarter=((cents_num%200)%100)//25 #value of 1 quarter is 25 cents
dime=(((cents_num%200)%100)%25)//10 #value of 1 dime is 10 cents
nickel=((((cents_num%200)%100)%25)%10)//5 #value of 1 nickel is 5 cents
penny= (((((cents_num%200)%100)%25)%10)%5)//1 #value of 1 penny is 1 cents

print(f"1. Toonies: {toonie}")
print(f"2. loonies: {loonie}")
print(f"3. Quarters: {quarter}")
print(f"4. Dimes: {dime}")
print(f"5. Nickels: {nickel}")
print(f"6. Pennies: {penny}")