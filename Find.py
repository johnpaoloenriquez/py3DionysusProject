"""Function that finds something the user wants in the text
    file and returns the line number of the item
"""
from menu import Get_Menu
def find_cart(Username,cart_name):
    with open(Username+"_cart.txt", "r") as f:
        #begin line is where the item is found
        #end line is where the item ends
        begin_line=0
        end_line=0
        lines=f.readlines()
        #loop through the txt file the 'i' is the line number
    for i in range(len(lines)):
        if cart_name+":" in lines[i]:
            begin_line=i+1
        if "end_of_"+cart_name in lines[i]:
            end_line=i-1
                
    #get the items using the begin_line and end_line
        cart_items=[]
        item_quantity=[]
        for i in range(begin_line, end_line):
            cart_items.append(int( lines[i].split("\t")[0] ))
            item_quantity.append(int(lines[i].split("\t")[1]))
    if cart_items==[]:
        print("Cart is empty")
    return cart_items, item_quantity

def Cart(cart_items, item_quantity):
    item_id, item_name, item_price,item_description=Get_Menu()
    cart_total = 0
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
    
