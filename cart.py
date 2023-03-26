from menu import Get_Menu
#from receipts import Save_Transaction, Transaction_List, Load_Transaction
import sys
import time
from receipts import Save_Transaction, Load_Transaction, Transaction_List
#displays the cart based on cart items and item quantity

def Cart(Cart_Items, Item_Quantity):
    item_id,item_name,item_price,item_description = Get_Menu()
    Cart_Total = 0
    print("---------------------------------------------------------------------")
    print("\t\t\t\tCART")
    print("---------------------------------------------------------------------")
    print("ID \tName\t\t\t\tPrice\t\tQuantity")
    
    for i in range(len(Cart_Items)):
        print(item_id[Cart_Items[i]], end='\t')
        print(item_name[Cart_Items[i]], end='\t\t\t')
        print("P"+str(item_price[Cart_Items[i]]), end='\t\t')
        print(Item_Quantity[i])

        Cart_Total += (item_price[Cart_Items[i]]*Item_Quantity[i])

    print("Total: P"+str(Cart_Total)+"\n")
    return Cart_Total

#finds the cart of the user
def find_cart(Username,Cart_Name):
    try:
        with open(Username+"_cart.txt", "r") as f:
            #begin line is where the item is found
            #end line is where the item ends
            begin_line=0
            end_line=0
            lines=f.readlines()
            #loop through the txt file the 'i' is the line number
            for i in range(len(lines)):
                if Cart_Name.lower()+":" in lines[i]:
                    begin_line=i+1
                if "end_of_"+Cart_Name.lower() in lines[i]:
                    end_line=i-1
                
        #get the items using the begin_line and end_line
            Cart_Items=[]
            Item_Quantity=[]
            for i in range(begin_line, end_line):
                Cart_Items.append(int(lines[i].split("\t")[0]))
                Item_Quantity.append( int( lines[i].split("\t")[1] ))
        if Cart_Items==[]:
            print("Cart is empty")
        #Find_Cart returns: Cart_Items, Item_Quantity
        return Cart_Items, Item_Quantity
    
    #File not found error
    except FileNotFoundError:
        print("Cart is empty")
        return [],[]
#checkout part of the shopping cart
def checkout(Username, Cart_Items, Item_Quantity):
    try:
        checkout_choice=0
        while checkout_choice!=1 and checkout_choice!=7:
            try:
                Cart_Total=Cart(Cart_Items, Item_Quantity)
                print("1 - Checkout")
                print("2 - Save Cart")
                print("3 - Load Saved Cart")
                print("4 - Delete Saved Cart")
                print("5 - Clear Cart")
                print("6 - Shop Again")
                print("7 - Logout")
                checkout_choice=int(input(""))
        
                if checkout_choice==1:
                    if Cart_Items==[]:
                        print("Cannot Checkout with an empty cart!")
                        break
                    print("Proceeding to checkout...")
                    shipping_details_choice=0
                    #Shipping Details
                    while shipping_details_choice!=1 and shipping_details_choice!=2:
                        try:
                            #Check first if user has account details saved
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
                                print("Would you like to use these details?")
                                Account_Details_Use=int(input("1 - Yes, 2 - No\n"))
                                if Account_Details_Use==1:
                                    break
                            else:
                                print("No Account Details Found")
                            print("Please enter your name: ")
                            name=input("")
                            print("Please enter your address: ")
                            address=input("")
                            print("Please enter your contact number: ")
                            contact=input("")
                            print("Please enter your email address: ")
                            email=input("")
                            #Ask user if they want to save their shipping details
                            print("Would you like to save your shipping details?")
                            print("1 - Yes, 2 - No")
                            #Save shipping details
                            shipping_details_choice=int(input(""))
                            #Username is defined on main function
                            
                            if shipping_details_choice==1:
                                with open(Username+"_account.txt","w") as f:
                                    f.writelines("Name: "+name+" \n")
                                    f.writelines("Address: "+address+" \n")
                                    f.writelines("Contact Number: "+contact+" \n")
                                    f.writelines("Email: "+email+ " \n")
                                print("Shipping details saved!")
                                time.sleep(1)
                            #If user doesn't want to save their shipping details just continue with the code
                        
                        
                        #IF NO FILE IS FOUND ASK USER IF THEY WANT TO SAVE THEIR SHIPPING DETAILS
                        #If user wants to save then save it otherwise just use the info for one transaction
                        except FileNotFoundError:
                            print("No Account Details Found")
                        
                            print("Please enter your name: ")
                            name=input("")
                            print("Please enter your address: ")
                            address=input("")
                            print("Please enter your contact number: ")
                            contact=input("")
                            print("Please enter your email address: ")
                            email=input("")
                        
                            print("\nWould you like to Save your Account Details?\n1 - Yes\n2 - No")
                            Account_Choice=int(input(""))
                            if Account_Choice==1:
                                with open(Username+"_account.txt","w") as f:
                                    f.writelines("Name: "+name+" \n")
                                    f.writelines("Address: "+address+" \n")
                                    f.writelines("Contact Number: "+contact+" \n")
                                    f.writelines("Email: "+email+ " \n")
                                print("Shipping details saved!")
                                time.sleep(1)

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
                    print("Your total is P"+str(Cart_Total))
                    Save_Transaction(Username, Cart_Items, Item_Quantity)
                    print("You have successfully placed an Order!")
                    return 0
                    #END OF CHECKOUT
                    
                    
                elif checkout_choice==2:
                    if Cart_Items==[]:
                        print("Cannot save an empty cart!")
                        continue
                    print("Please enter the name of your cart:")
                    cart_name=input("")
                    Save_Cart(Username,cart_name.lower(),Cart_Items,Item_Quantity)
                    print("Cart saved!")
                
                
                elif checkout_choice==3:
                    Cart_List=Load_Cart(Username)
                    if Cart_List==[]:
                        print("You have no saved carts")
                        time.sleep(1)
                        break
                    view_cart=input("\nEnter the Cart you wish to view: ")
                    Cart_Name=Cart_List[int(view_cart)-1]
                    Cart_Items,Item_Quantity=find_cart(Username,Cart_Name)
                    time.sleep(1)
                    
                elif checkout_choice==4:
                    Cart_List=Load_Cart(Username)
                    if Cart_List==[]:
                        print("You have no saved carts")
                        time.sleep(1)
                        break
                    view_cart=input("\nEnter the Cart you wish to delete: ")
                    Cart_Name=Cart_List[int(view_cart)-1]
                    Delete_Cart(Username,Cart_Name)
                    
                    
                    

    
                elif checkout_choice==5:
                    print("Clearing cart...")
                    Cart_Items=[]
                    Item_Quantity=[]
                    Delete_Cart(Username, "current_cart")
                    Cart_Total = 0
                    print("Cart cleared!")
        
                elif checkout_choice==6:
                    print("Going back to shopping...")
                    continue_shopping=1
                    continue_shopping2=1
                    break
                elif checkout_choice==7:
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
    except ValueError:
        print("Invalid input")
        time.sleep(1)

#This function saves the cart items
def Save_Cart(Username,Cart_Name,Cart_Items,Item_Quantity):
    while True:
        try:
            with open(Username+"_cart.txt", "r") as f:
                lines=f.readlines()
                for i in lines:
                    if Cart_Name.lower()+":" in i:
                        print("Cart already exists")
                        return
                with open(Username+"_cart.txt", "a") as f:
                    f.writelines("\n\n")
                    f.writelines(Cart_Name.lower()+": \n")
                    for i in range(len(Cart_Items)):
                        f.writelines(str(Cart_Items[i])+"\t"+str(Item_Quantity[i])+"\t\n")
                    f.writelines("\nend_of_"+Cart_Name.lower() +" \n")
                    print("Cart saved")
                    return
        except FileNotFoundError:
            with open(Username+"_cart.txt", "w") as f:
                f.writelines("format: \n")
                f.writelines("item_id\titem_quantity\t \n")
                f.writelines("\nend_of_(name of cart) \n")
                f.writelines("\n")
                for i in range(len(Cart_Items)):
                    f.writelines(str(Cart_Items[i])+"\t"+str(Item_Quantity[i])+"\t\n")
                f.writelines("\nend_of_current_cart \n")
            print("")
            print("Cart Database Created")
            print("Please Try Again")

#loads cart items from the txt file
def Load_Cart(Username):
    while True:
        try:
            with open (Username+"_cart.txt", "r") as f:
                lines=f.readlines()
                Cart_List=[]
                for i in lines:
                    if "format" in i or "current_cart" in i:
                        continue
                    if ":" in i:
                        Cart_List.append(i.rstrip(": \n")) 
                print("Cart List:")
                for i in range(len(Cart_List)):
                    print(str(i+1)+" - "+Cart_List[i])
            return Cart_List
        except FileNotFoundError:
            print("No existing Carts, Please create a cart first!")
            time.sleep(1)
            break

        
def Delete_Cart(Username, Cart_Name):
    try:
        with open(Username+"_cart.txt", "r") as f:
            #begin line is where the item is found
            #end line is where the item ends
            begin_line=0
            end_line=0
            
            lines=f.readlines()
            ptr=1
            #loop through the txt file the 'i' is the line number
            for i in range(len(lines)):
                if Cart_Name.lower()+":" in lines[i]:
                    begin_line=i
                if "end_of_"+Cart_Name.lower() in lines[i]:
                    end_line=i+1
            if begin_line==0 and end_line==0:
                print("Cart not found")
                return
            with open(Username+"_cart.txt", "w") as fw:
                for line in lines:
                    if ptr<begin_line or ptr>end_line:
                        fw.write(line)
                    ptr+=1
    
    #File not found error
    except FileNotFoundError:
        print("Cart is empty")
        return [],[]
    


#SAMPLE OUTPUT FOR TESTING PURPOSES

#Username="Endomou"
#Cart_Name = "current_cart"
#Cart_Items, Item_Quantity =find_cart(Username,"current_cart")
#Cart_Total=Cart(Cart_Items, Item_Quantity)
#Save_Cart(Username, Cart_Name, Cart_Items, Item_Quantity)
#checkout(Username, Cart_Items, Cart_Total)
#Delete_Cart(Username, Cart_Name)