import datetime
from menu import Get_Menu

def Save_Transaction(Username, Cart_Items, Item_Quantity, name, address, contact, email, payment):
    item_id, item_name, item_price, Item_Description = Get_Menu()
    Cart_Total=0
    for i in range(len(Cart_Items)):
        Cart_Total += (item_price[Cart_Items[i]]*Item_Quantity[i])
    with open(Username.lower()+"_receipts.txt", "a") as f:
        f.write("\n------------------------------------------------------------------------------------------------")
        f.write("\nDate: "+str(datetime.datetime.now())+"")
        f.write("\nID \t"+"Name".ljust(63)+"Price\t\tQuantity")
        for i in range(len(Cart_Items)):
            f.write("\n"+str(item_id[Cart_Items[i]])+"\t"+item_name[Cart_Items[i]].ljust(63)+""+str(item_price[Cart_Items[i]])+"\t\t"+str(Item_Quantity[i]))
        f.write("\nTotal: P"+str(Cart_Total)+"\n")
        f.writelines("\nShipping Details:\n")
        f.write("Name: "+name)
        f.write("Address: "+address)
        f.write("Contact: "+contact)
        f.write("Email: "+email)
        f.write("Payment Method: "+payment)
        f.write("\n------------------------------------------------------------------------------------------------\n")
        
def Load_Transaction(Username, date):
    try:
        print("Loading transaction history")
        with open(Username.lower()+"_receipts.txt", "r") as f:
            lines = f.readlines()
        Begin_Line=0
        End_Line=0
        Transaction=[]
        for i in range(len(lines)):
            if date in lines[i]:
                Begin_Line=i-1
    
        for i in range(Begin_Line+1, len(lines)):
            if "-------" in lines[i]:
                End_Line=i
                break
        
        for i in range(Begin_Line, End_Line):
            Transaction.append(lines[i])
        return Transaction
    except FileNotFoundError:
        print("Transaction history file does not exist")
        print("Creating new file for transaction history")
        with open(Username.lower()+"_receipts.txt", "w") as f:
            f.writelines("")

def Transaction_List(Username):
    while True:
        try:
            Transaction_List=[]
            with open(Username.lower()+"_receipts.txt", "r") as f:
                lines = f.readlines()
                for i in lines:
                    if "Date: " in i:
                        i=i.rstrip("\n")
                        Transaction_List.append(i.split(": ")[1])
            return Transaction_List
        except FileNotFoundError:
            with open(Username.lower()+"_receipts.txt", "w") as f:
                f.writelines("")
            print("Transaction history file does not exist")
            print("Creating new file for transaction history")

#Sample Tests Below
        
#Username="Endomou"
#Cart_Name="rtx4090"
#item_id,item_name,item_price,item_description = Get_Menu()
#Cart_Items, Item_Quantity = cart.find_cart(Username, Cart_Name)
#Cart_Total=0
#for i in range(len(Cart_Items)):
#    Cart_Total += (item_price[Cart_Items[i]]*Item_Quantity[i])
#Save_Transaction(Username, Cart_Items, Item_Quantity)
#Transaction=Load_Transaction(Username, "2023-03-26 21:18:28.534556")
