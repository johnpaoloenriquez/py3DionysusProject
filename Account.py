import maskpass



def SignIn():
    '''function that accepts a username and a password
    and signs in if the password is correct and exits the program
    after 5 incorrect attempts
    '''
    attempt = 0
    while attempt<5:
        UsernameIsPresent = False
        Username = input("Enter your Username: ")

        Password = maskpass.askpass(prompt="Password:", mask="*")
        file=open("Accounts.txt","r")
        file_read=file.readlines()
        #THIS IS NOT DONE
        #check if username is present then check the password after
        
        for i in file_read:
            #Username is not case sensitive, Password is case sensitive
            if "."+Username.lower()+" " in i.lower() and ","+Password+" " in i:
                UsernameIsPresent = True
                break
        if UsernameIsPresent == True:
            file.close()
            return Username
        elif attempt >= 0 and attempt < 4:
            print("Invalid Username or Password, Please Try again")
            attempt+=1
            file.close()
        else:
            print("Too many attempts, Please Try again later")
            exit()

def SignUp():
    while True:
        UsernameIsTaken = False
        Username=input("Create your username:")
        #read from database if username exists
        file=open("Accounts.txt","r")
        file_read=file.readlines()
        #loop through the database and check if username exists
        for i in file_read:
            if "."+Username.lower()+" " in i.lower():
                UsernameIsTaken = True
                break
        if UsernameIsTaken==True:
            print("Username is already taken, Please try again")
            file.close()
            continue
        file.close()
        Password = maskpass.askpass(prompt="Create your Password:", mask="*")
        ConfirmPassword = maskpass.askpass(prompt="Confirm your Password:", mask="*")
        if Password == ConfirmPassword:
            file=open("Accounts.txt","a")
            file.write("."+Username + " ," + Password +" \n")
            print("Account created successfully")
            file.close()
            #append to Accounts.txt
            return Username
        else:
            print("Password does not match, Please try again")
            continue