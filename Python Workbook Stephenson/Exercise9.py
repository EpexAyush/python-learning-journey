#calculating the compound interest:
# A=P(1+(r/100))^n  
#--------------where-----------------: 
# A= total amount after that year.
# r= interest rate.
# n= number of years.
# P= deposit amount

dep_amt=float(input("Enter the deposit amount: "))
int_rate=4 #interest rate is 4% per year

amount_1= dep_amt*(1+(4/100))**1
amount_2=dep_amt*(1+(4/100))**2
amount_3=dep_amt*(1+(4/100))**3
amount_4=dep_amt*(1+(4/100))**4
print(f"Amount after 1 year: {amount_1:.2f}")
print(f"Amount after 2 year: {amount_2:.2f}")
print(f"Amount after 3 year: {amount_3:.2f}")
print(f"Amount after 4 year: {amount_4:.2f}")
