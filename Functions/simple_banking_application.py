'''def check_balance():
    print(f"Current Balance is: {balance}")



def deposit(deposit_amount):
    global balance
    if deposit_amount<0:
        print("Enter a Valid Deposit Amount.")
    else:
        balance+=deposit_amount
        print(f"Your Updated Balance is:{balance}")
    


def withdrawl(withdrawl_amount):
    global balance
    if withdrawl_amount<=0:
        print("Enter a valid withdrawl amount.")
    elif withdrawl_amount>balance:
        print("Insufficient Funds.")
    else:
        balance-=withdrawl_amount
        print(f"Amount {withdrawl_amount} has been successfully withdrawn.")
        print(f"Your updated balance is: {balance}")


balance=0
print("==========Welcome to XYZ Bank=============")
while True:
    
    print("1. Check balance.")
    print("2. Deposit an amount.")
    print("3. Withdrawl an amount.")
    print("4. Quit.")
    choice=float(input("Enter your choice(1-4): "))

    if choice==1:
        print("---------------------------")
        check_balance()
        print("---------------------------\n")

    elif choice==2:
        print("----------------------------")
        deposit_amount=float(input("Enter Deposit Amount: "))
        deposit(deposit_amount)
        print("----------------------------\n")

    elif choice==3:
        print("-----------------------------")
        withdrawl_amount=float(input("Enter Withdrawl Amount: "))
        withdrawl(withdrawl_amount)

    elif choice==4:
        break
    else:
        print("Invalid input!")
        print("-----------------------------\n")
    print("For more services you can choice again.")
    
print("-----------------------------------------------")
print("Thank you for using our banking application.")
print("-----------------------------------------------")
'''



x=2
y=8
z=x+y/2
print(x+z)
print("-----------")
x=2
y=8
z=x+y//2

print(x+z)
print("----------")
