username=input("Enter Your Username: ")
if username=="admin":
    user_pass=input("Enter Password: ")
    if user_pass=="1234":
        print("Access Granted")
    else:
        print("Invalid Password")
else:
    print("User Not Found")