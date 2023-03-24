"""This is the main code where most the functions, subfunctions, etc. will be executed
when working on a feature, make sure it properly works before adding here
"""

from Account import SignIn,SignUp
#main function
print("Log in or Sign up First before accessing the system:")
print("1 - Login")
print("2 - Signup")
#Login or Sign up Part
LogIn=input("")
if LogIn=='1':
    Username=SignIn()
elif LogIn=='2':
    Username=SignUp()
    
print("Welcome, "+ Username)

print("Would you like to:")
print("1 - Go shopping")
print("2 - Check your cart")
print("3 - Check your orders")
print("4 - Check your account details")
print("5 - Log out")
shopping_choice=input("")
