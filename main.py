from Account import SignIn,SignUp
from menu import Get_Menu, Display_Menu
from cart import find_cart, checkout, Save_Cart, Delete_Cart, Load_Cart
from receipts import Load_Transaction, Transaction_List
import sys
import time

#main function
LogIn=0
while LogIn!=1 and LogIn!=2:
    print("Log in or Sign up First before accessing the system:")
    print("1 - Login")
    print("2 - Signup")
    #Login or Sign up Part
    try:
        LogIn=int(input(""))
        if LogIn==1:
            Username=SignIn()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        elif LogIn==2:
            Username=SignUp()
        else:
            print("Please enter a valid input")
            time.sleep(1)
    #Catch error when file is not found
    except FileNotFoundError:
        print("File not found")
        print("Creating new file...")
        with open("accounts.txt","w") as f:
            f.write("")
        print("File created!")
        print("Please try again")
        
    #catch error when user inputs a string instead of an integer
    except ValueError:
        print("Please enter a valid input")
        time.sleep(1)
print("Welcome, "+ Username)

shopping_choice=0

while shopping_choice!=5:
    try:
        print("Would you like to:")
        print("1 - Go shopping") 
        print("2 - Check your cart")
        print("3 - Check your Previous orders")
        print("4 - Check your account details")
        print("5 - Log out")
        shopping_choice=int(input(""))
        
        #1 - GO SHOPPING
        
        if shopping_choice==1:
            
            #Declare variables for the cart
            Cart_Items, Item_Quantity = find_cart(Username,"current_cart")
            Cart_Total=0
            #gets items from the menu
            item_id,item_name,item_price,item_description = Get_Menu()
            
            
            #These values make the loops run
            continue_shopping=1
            continue_shopping2=1
    
            #if the user wants to continue shopping after viewing the cart it will be looped
            while continue_shopping2==1:
        
                #this loop is for the menu if the user wants to continue shopping after adding an item to the cart
                while continue_shopping==1:
            
                    #try and except is used to catch errors
                    #if the user inputs a string instead of an integer, it will catch the error
                    try:
                        Display_Menu(item_id, item_name, item_price, item_description)
            
                        #getting the item id
                        print("Enter the id of the item you wish to buy:", end=" ")
                        item=int(input(""))
                
                        #Display Item Details
                        print(item_name[item], end=' ')
                        print('P'+str(item_price[item]))
                        print(item_description[item])
    
                        quantity=int(input("Quantity: "))
        
                        if item in Cart_Items:
                            Item_Quantity[Cart_Items.index(item)] += quantity
                        if quantity!=0 and item not in Cart_Items:
                            Item_Quantity.append(quantity)
                            Cart_Items.append(item)
        
                        print("\n1 - Continue Shopping")
                        print("2 - View Cart")
                        #MENU ENDS HERE IF USER INPUTS anything other than 1
                        continue_shopping=int(input(""))
                        
            
                    #catch the error with the code below
                    except:
                        print("Please enter a valid input")
                        time.sleep(1)
                Save_Cart(Username,"current_cart",Cart_Items,Item_Quantity)
                continue_shopping2=checkout(Username,Cart_Items,Item_Quantity)
                
                if continue_shopping2!=1:
                    print("Would you like to shop again?")
                    continue_shopping2=int(input("1 - Yes\n2 - No\n"))
                    
                if continue_shopping2==1:
                    continue_shopping=1
                    
                elif continue_shopping2==2:
                    print("Thank you for shopping with us!")
                    print("Please come Again")
                    continue_shopping=0
                    continue_shopping2=0
                    shopping_choice=5
            
        #END OF 1 - GO SHOPPING

        #2 - CHECK CART
        elif shopping_choice==2:
            Cart_Check=1
            while Cart_Check==1 or Cart_Check==2:
                try:
                    print("Would you like to:")
                    print("1 - View Current Cart")
                    print("2 - View list of saved carts")
                    print("3 - Delete a saved cart")
                    print("4 - Go back")
                    Cart_Check=int(input(""))
                
                    if Cart_Check==1:
                        Cart_Name="current_cart"
                        Cart_Items,Item_Quantity=find_cart(Username,Cart_Name)
                        if Cart_Items==[] or None:
                            print("Your Current Cart is empty")
                            time.sleep(1)
                            break
                        try:
                            checkout(Username,Cart_Items,Item_Quantity)
                        except:
                            print("Your cart is empty")
                            time.sleep(1)
                    elif Cart_Check==2:
                        Cart_List=Load_Cart(Username)
                        if Cart_List==[]:
                            print("You have no saved carts")
                            time.sleep(1)
                            break
                        view_cart=input("\nEnter the Cart you wish to view: ")
                        Cart_Name=Cart_List[int(view_cart)-1]
                        Cart_Items,Item_Quantity=find_cart(Username,Cart_Name)
                        #break out the loop
                        Cart_Check=3
                        
                    elif Cart_Check==3:
                        try:
                            Cart_List=Load_Cart(Username)
                            if Cart_List==[] or Cart_List==None:
                                print("You have no saved carts")
                                time.sleep(1)
                                break
                            view_cart=input("\nEnter the Cart you wish to delete: ")
                            Cart_Name=Cart_List[int(view_cart)-1]
                            Delete_Cart(Username,Cart_Name)
                        except:
                            print("Please enter a valid input")
                            time.sleep(1)
                    elif Cart_Check==4:
                        break
                    else:
                        print("Please enter a valid input")
                        time.sleep(1)
                        
                except ValueError:
                    print("Please enter a valid input")
                    time.sleep(1)
                #END OF 2 - CHECK CART

        #3 - CHECK PREVIOUS ORDERS
        elif shopping_choice==3:
            Transaction_Number=1
            while Transaction_Number!=0:
                try:
                    print("Transaction List:")
                    Transac_List=Transaction_List(Username)
                    for i in range(len(Transac_List)):
                        print(str(i+1)+" - "+Transac_List[i])
                    print("Enter the transaction number you wish to view:")
                    Transaction_Number=int(input("Input 0 if you wish to go back\n"))
                    Transaction=Load_Transaction(Username,Transac_List[Transaction_Number-1])
                    for i in Transaction:
                        print(i)
                except ValueError:
                    print("Please enter a valid input")
            
        #END OF 3 - CHECK PREVIOUS ORDERS

        #4 - CHECK ACCOUNT DETAILS
        elif shopping_choice==4:
            Account_Choice=0
            while Account_Choice!=1 or Account_Choice!=2:
                try:
                    name=""
                    address=""
                    contact=""
                    email=""
                    #Get Account Details from the text file
                    with open(Username+"_account.txt","r") as f:
                        account=f.readlines()
                        for line in account:
                            if "Name: " in line:
                                name=line.split(": ")[1]
                            elif "Address: " in line:
                                address=line.split(": ")[1]
                            elif "Contact Number: " in line:
                                contact=line.split(": ")[1]
                            elif "Email: " in line:
                                email=line.split(": ")[1]
                    if name!="" or address!="" or contact!="" or email!="":
                        print("Name: "+name)
                        print("Address: "+address)
                        print("Contact Number: "+contact)
                        print("Email: "+email) 
                    else:
                        print("No Account Details Found")
                        
                        
                    print("\n Would you like to:")
                    print("1 - Edit Account Details")
                    print("2 - Go Back")
                    Account_Choice=int(input(""))
                    if Account_Choice==1:
                        print("Please enter your name: ")
                        name=input("")
                        print("Please enter your address: ")
                        address=input("")
                        print("Please enter your contact number: ")
                        contact=input("")
                        print("Please enter your email address: ")
                        email=input("")
                        
                        with open(Username+"_account.txt","w") as f:
                            f.writelines("Name: "+name+" \n")
                            f.writelines("Address: "+address+" \n")
                            f.writelines("Contact Number: "+contact+" \n")
                            f.writelines("Email: "+email+ " \n")
                        print("Shipping details saved!")
                        time.sleep(1)
                        break
                    elif Account_Choice==2:
                        break
                        
                        
                                
                                
                except FileNotFoundError:
                    print("No Account Details Found")
                    Account_Choice=int(input("1 - Save Account Details\n2 - Go Back\n"))
                    
                    if Account_Choice==1:
                        print("Please enter your name: ")
                        name=input("")
                        print("Please enter your address: ")
                        address=input("")
                        print("Please enter your contact number: ")
                        contact=input("")
                        print("Please enter your email address: ")
                        email=input("")
                        
                        with open(Username+"_account.txt","w") as f:
                            f.writelines("Name: "+name+" \n")
                            f.writelines("Address: "+address+" \n")
                            f.writelines("Contact Number: "+contact+" \n")
                            f.writelines("Email: "+email+ " \n")
                        print("Shipping details saved!")
                        time.sleep(1)
                        break
                    elif Account_Choice==2:
                        break
                    else:
                        print("Please enter a valid input")
                        time.sleep(1)
                except ValueError:
                    print("Please enter a valid input")
                    time.sleep(1)
                #END OF 4 - CHECK ACCOUNT DETAILS



        #5 - LOG OUT
        elif shopping_choice==5:
            print("Logging out...")
            print("Thank you for shopping with us!")
            print("Come Again!")
            sys.exit()
        else:
            print("Please enter a valid input")
            time.sleep(1)

    except ValueError:
        print("\nPlease enter a valid input \n")
        time.sleep(1)