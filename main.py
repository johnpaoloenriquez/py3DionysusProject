"""This is the main code where most the functions, subfunctions, etc. will be executed
when working on a feature, make sure it properly works before adding here
"""


import maskpass
dbUsername = "john"
dbPassword = "johndoe123"
UserName=""
Password=""
def SignIn():
    '''function that accepts a username and a password
    and signs in if the password is correct and exits the program
    after 5 incorrect attempts
    '''
    Username = input("Enter your Username: ")
    Password = maskpass.askpass(prompt="Password:", mask="*")
    attempt = 0
    while attempt<5:
        if Username.lower() == dbUsername.lower() and Password == dbPassword :
            print("Welcome " + Username )
        elif attempt > 0 and attempt < 4:
            print("Incorrect Password, Please Try again")
            attempt+=1
        else:
            print("Too many attempts, Please Try again later")
            break
def SignUp():
    UserName=input("Create your username:")
    while Password!=ConfirmPassword:
        Password = maskpass.askpass(prompt="Create your Password:", mask="*")
        ConfirmPassword = maskpass.askpass(prompt="Confirm your Password:", mask="*")
    




#main function
print("Log in or Sign up First before accessing the system:")
print("1 - Login")
print("2 - Signup")
#Login or Sign up Part
LogIn=input("")
if LogIn=='1':
    SignIn()
elif LogIn=='2':
    SignUp()


print("Welcome " + UserName)

