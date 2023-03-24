"""cart system
features:
- add to cart items and it will be stored in a cart 
- when user goes to the cart user should be given option to checkout or continue shopping 
- extra features:
    - saving and loading cart with naming system
        - This feature allows users to save different carts and name them as well for later 
        

"""
#this will be connected with menu.pyimport Menuimport Menu

cart_items=[]
item_quantity=[]
cart_total = 0
#gets items from the menu

item_id=Menu.item_id
item_name=Menu.item_name
item_price=Menu.item_price
item_description=Menu.item_description

#These values make the loop run
continue_shopping=1
continue_shopping2=1

#this part is the shopping part
while continue_shopping2==1:
    #displaying the menu
    while continue_shopping==1:
        #try and except is used to catch errors
        #if the user inputs a string instead of an integer, it will catch the error
        try:
            print("---------------------------------------------------------------------")
            print("\t\t\t\tMENU")
            print("---------------------------------------------------------------------")
            print("ID \tName\t\t\t\tPrice\t\tDescription")
            for i in range(len(item_id)):
                print(item_id[i], end='\t')
                print(item_name[i], end='\t\t\t')
                print("P"+str(item_price[i]), end='\t\t')
                print(item_description[i])
            
            #getting the item id
            print("Enter the id of the item you wish to buy:", end=" ")
            item=int(input(""))
    
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
            continue_shopping=int(input(""))
            #MENU ENDS HERE IF USER INPUTS 2
        #catch the error with the code below
        except:
            print("Please enter a valid input")
        
        
    #Cart System
    print("---------------------------------------------------------------------")
    print("\t\t\t\tCART")
    print("---------------------------------------------------------------------")
    print("ID \tName\t\t\t\tPrice\t\tQuantity")
    for i in range(len(cart_items)):
        print(item_id[cart_items[i]], end='\t')
        print(item_name[cart_items[i]], end='\t\t\t')
        print("P"+str(item_price[cart_items[i]]), end='\t\t')
        print(item_quantity[i])
    
        cart_total += (item_price[cart_items[i]]*item_quantity[i])

    print("Total: P"+str(cart_total))


    checkout_choice=0
    while checkout_choice!=1 and checkout_choice!=2 and checkout_choice!=4:
        try:
            print("1 - Checkout")
            print("2 - Clear Cart")
            print("3 - Shop Again")
            print("4 - Logout")
            checkout_choice=int(input(""))
        
            if checkout_choice==1:
                print("Proceeding to checkout...")
            
                print("Please enter your name:")
                name=input("")
                print("Please enter your address:")
                address=input("")
                print("Please enter your contact number:")
                contact=input("")
                print("Please enter your email address:")
                email=input("")
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
                exit()
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input")
    