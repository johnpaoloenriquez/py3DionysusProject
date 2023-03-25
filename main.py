from Account import SignIn,SignUp
from Menu import Get_Menu, Display_Menu
from Find import find_cart, Cart
import sys
import time

#main function
LogIn=0
while LogIn!=1 and LogIn!=2:
    print("Log in or Sign up First before accessing the system:")
    print("1 - Login")
    print("2 - Signup")
    #Login or Sign up Part
    LogIn=int(input(""))
    if LogIn==1:
        Username=SignIn()
    elif LogIn==2:
        Username=SignUp()
    else:
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
            cart_items=[]
            item_quantity=[]
            cart_total = 0
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
        
                        if item in cart_items:
                            item_quantity[cart_items.index(item)] += quantity
                        if quantity!=0 and item not in cart_items:
                            item_quantity.append(quantity)
                            cart_items.append(item)
        
                        print("\n1 - Continue Shopping")
                        print("2 - View Cart")
                        #MENU ENDS HERE IF USER INPUTS anything other than 1
                        continue_shopping=int(input(""))
            
                    #catch the error with the code below
                    except:
                        print("Please enter a valid input")
                        time.sleep(1)
                Cart(cart_items, item_quantity)
            
            
                checkout_choice=0
                while checkout_choice!=1 and checkout_choice!=2 and checkout_choice!=4:
                    try:
                        print("1 - Checkout")
                        print("2 - Clear Cart")
                        print("3 - Shop Again")
                        print("4 - Logout")
                        checkout_choice=int(input(""))
        
                        if checkout_choice==1:
                            if cart_items==[]:
                                print("Cannot Checkout with an empty cart!")
                                break
                            print("Proceeding to checkout...")

                            #Shipping Details
                            print("Please enter your name:")
                            name=input("")
                            print("Please enter your address:")
                            address=input("")
                            print("Please enter your contact number:")
                            contact=input("")
                            print("Please enter your email address:")
                            email=input("")
                
                            #Ask user if they want to save their shipping details
                            print("Would you like to save your shipping details?")
                            print("1 - Yes, 2 - No")
                
                            #Save shipping details
                            shipping_details_choice=int(input(""))
                            #Username is defined on main function
                            Account_Info=open(Username+".txt","w")
                            if shipping_details_choice==1:
                                Account_Info.write(name+" \n")
                                Account_Info.write(address+" \n")
                                Account_Info.write(contact+" \n")
                                Account_Info.write(email+ " \n")
                                print("Shipping details saved!")
                            Account_Info.close()
                            #If user doesn't want to save their shipping details just continue with the code
                    
                            print("Please enter your payment method:")
                            payment=input("")
                    
                            print("Thank you for your purchase!")
                            print("Your order will be delivered to:")
                            print(name)
                            print(address)
                            print(contact)
                            print(email)
                            print("Your payment method is:")
                            print(payment)
                            print("Your total is P"+str(cart_total))
                
                            print("Would you like to shop again?")
                            continue_shopping2=int(input("1 - Yes\n2 - No\n"))
                            print("Thank you for shopping with us!")
                            print("Please come Again")

    
                        elif checkout_choice==2:
                            print("Clearing cart...")
                            cart_items=[]
                            item_quantity=[]
                            cart_total = 0
                            print("Cart cleared!")
        
                        elif checkout_choice==3:
                            print("Going back to shopping...")
                            continue_shopping=1
                            break
                        elif checkout_choice==4:
                            print("Logging out...")
                            print("Thank you for shopping with us!")
                            print("Goodbye!")
                            #This will exit the program
                            continue_shopping=0
                            continue_shopping2=0
                            shopping_choice=5
                            sys.exit()
                        else:
                            print("Invalid input")
                            time.sleep(1)
                    except ValueError:
                        print("Invalid input")
                        time.sleep(1)
        #END OF 1 - GO SHOPPING

        #2 - CHECK CART
        elif shopping_choice==2:
            cart_items, item_quantity=find_cart(Username,"current_cart")
            Cart(cart_items, item_quantity)
    

        #3 - CHECK PREVIOUS ORDERS
        elif shopping_choice==3:
            pass


        #4 - CHECK ACCOUNT DETAILS
        elif shopping_choice==4:
            pass


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