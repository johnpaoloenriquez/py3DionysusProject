from Account import SignIn,SignUp
from menu import Get_Menu, Display_Menu
from cart import Cart,find_cart, checkout, Save_Cart, Delete_Cart, Load_Cart, clear
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
        clear()
    #Catch error when file is not found  
    except FileNotFoundError:
        with open("accounts.txt","w") as f:
            f.write("")
        
    #catch error when user inputs a string instead of an integer
    except ValueError:
        print("Please enter a valid input")
        time.sleep(1)
clear()
print("Welcome, "+ Username)

#get current cart items
Cart_Items, Item_Quantity = [] , []
Cart_Total=0
shopping_choice=0

while shopping_choice!=9:
    try:
        #Save_Cart(Username,"current_cart",Cart_Items,Item_Quantity)
        print("Would you like to:")
        print("1 - Go shopping") 
        print("2 - View your cart")
        print("3 - Checkout")
        print("4 - Save Cart")
        print("5 - View saved carts")
        print("6 - Clear Cart")
        print("7 - Check your Previous orders")
        print("8 - Check your account details")
        print("9 - Log out")
        shopping_choice=int(input(""))
        clear()
        #1 - GO SHOPPING
        
        if shopping_choice==1:
            #gets items from the menu
            item_id,item_name,item_price,item_description = Get_Menu()
            
            #These values make the loops run
            continue_shopping=1
            while continue_shopping==1:
            
                #try and except is used to catch errors
                #if the user inputs a string instead of an integer, it will catch the error
                try:
                    Display_Menu(item_id, item_name, item_price, item_description)

                    #getting the item id
                    print("Enter the id of the item you wish to buy:", end=" ")
                    item=int(input(""))
                    clear()
                    #Display Item Details
                    print(item_name[item], end=' - ')
                    print('P'+str(item_price[item]))
                    print("\nDescription:")
                    print(item_description[item])
                        
                    quantity=int(input("Quantity: "))
                        
                    if item in Cart_Items:
                        Item_Quantity[Cart_Items.index(item)] += quantity
                    if quantity!=0 and item not in Cart_Items:
                        Item_Quantity.append(quantity)
                        Cart_Items.append(item)
                    
                    Cart_Total=Cart(Cart_Items, Item_Quantity)
                    time.sleep(1)
                    print("\n1 - Continue Shopping")
                    #print("2 - View your cart")
                    print("2 - Go back to main menu")
                    #MENU ENDS HERE IF USER INPUTS anything other than 1
                    continue_shopping=int(input(""))
                    
                    #if continue_shopping==2:
                    #    Cart_Total=Cart(Cart_Items, Item_Quantity)
                    #    time.sleep(1)
                    clear()
            
                #catch the error with the code below
                except:
                    print("Please enter a valid input")
                    time.sleep(1)
    
            
        #END OF 1 - GO SHOPPING

        #2 - CHECK CART
        elif shopping_choice==2:
            Cart_Total=Cart(Cart_Items, Item_Quantity)
            time.sleep(1)
        #END OF 2 - CHECK CART
        
        
        #3 - CHECKOUT
        elif shopping_choice==3:
            Cart_Items,Item_Quantity,Cart_Total=checkout(Username,Cart_Items,Item_Quantity, Cart_Total)
            time.sleep(1)

        #4 - SAVE CART
        elif shopping_choice==4:
            if Cart_Items==[]:
                print("Cannot save an empty cart!")
                time.sleep(1)
                continue
            print("Please enter the name of your cart:")
            cart_name=input("")
            check=Save_Cart(Username,cart_name.lower(),Cart_Items,Item_Quantity)
            if check ==True:
                print("Cart saved!")
                time.sleep(1)
            else:
                print("Cart name already exists! Please delete first")
                time.sleep(1)
                
        #5 - View saved carts
        elif shopping_choice==5:
            while True:
                print("1 - View Named Cart")
                print("2 - Load Named Cart into Current Cart")
                print("3 - Delete Named Cart")
                print("0 - Go back to the main menu")
                Named_Cart_Choice=int(input(""))
                if Named_Cart_Choice==0:
                    break
                Cart_List=Load_Cart(Username)
                if Cart_List==[]:
                    print("You have no saved carts")
                    time.sleep(1)
                    
                elif Named_Cart_Choice==1:
                    View_Cart_Choice=int(input("Enter the number of the cart you wish to view: "))
                    Cart_Name=Cart_List[int(View_Cart_Choice)-1]
                    
                    View_Cart_Items,View_Item_Quantity=find_cart(Username,Cart_Name)
                    Cart(View_Cart_Items, View_Item_Quantity)
                    time.sleep(2)
                elif Named_Cart_Choice==2:
                    Load_Cart_Choice=int(input("Enter the number of the cart you wish to load: "))
                    Cart_Name=Cart_List[int(Load_Cart_Choice)-1]
                    Cart_Items,Item_Quantity=find_cart(Username,Cart_Name)
                    print("Cart loaded!")
                    time.sleep(1)
                    
                elif Named_Cart_Choice==3:
                    if Cart_List==[]:
                        print("You have no saved carts")
                        time.sleep(1)
                        break
                    view_cart=input("\nEnter the Cart you wish to delete: Enter 0 to exit\n")
                    Cart_Name=Cart_List[int(view_cart)-1]
                    Delete_Check=Delete_Cart(Username,Cart_Name)
                    if Delete_Check==True:
                        print("Cart deleted!")
                        time.sleep(1)
                        
                else:
                    print("Please enter a valid input")
                    time.sleep(1)
        #6 - CLEAR CART
        elif shopping_choice==6:
            print("Clearing cart...")
            Cart_Items.clear()
            Item_Quantity.clear()
            Cart_Total = 0
            print("Cart cleared!")
            time.sleep(1)
        
        #7 - CHECK PREVIOUS ORDERS
        elif shopping_choice==7:
            Transaction_Number=1
            while Transaction_Number!=0:
                try:
                    print("Transaction List:")
                    Transac_List=Transaction_List(Username)
                    for i in range(len(Transac_List)):
                        print(str(i+1)+" - "+Transac_List[i])
                    print("Enter the transaction number you wish to view:")
                    Transaction_Number=int(input("Input 0 if you wish to go back\n"))
                    if Transaction_Number==0:
                        break
                    Transaction=Load_Transaction(Username,Transac_List[Transaction_Number-1])
                    for i in Transaction:
                        print(i)
                    time.sleep(1)
                except ValueError:
                    print("Please enter a valid input")
        #END OF 3 - CHECK PREVIOUS ORDERS
        
        #8 - CHECK ACCOUNT DETAILS
        elif shopping_choice==8:
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
                    else:
                        print("Please enter a valid input")
                        time.sleep(1)
                        
                        
                                
                                
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



        #9 - LOG OUT
        elif shopping_choice==9:
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