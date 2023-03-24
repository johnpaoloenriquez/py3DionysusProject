"""cart system
features:
- add to cart items and it will be stored in a cart 
- when user goes to the cart user should be given option to checkout or continue shopping 
- extra features:
    - saving and loading cart with naming system
        - This feature allows users to save different carts and name them as well for later 
        

"""
#this will be connected with menu.pyimport Menu
import Menu
continue_shopping="1"
cart_items=[]
item_quantity=[]
cart_total = 0

item_id=Menu.item_id
item_name=Menu.item_name
item_price=Menu.item_price
item_description=Menu.item_description
while continue_shopping=="1":
    print("--------------------")
    print("MENU")
    print("--------------------")
    print("ID \tName\t\t\t\tPrice\t\tDescription")
    for i in range(len(item_id)):
        print(item_id[i], end='\t')
        print(item_name[i], end='\t\t\t')
        print("P"+str(item_price[i]), end='\t\t')
        print(item_description[i])
    
    print("Enter the id of the item you wish to buy:")
    item=int(input(""))
    
    print(item_name[item], end=' ')
    print('P'+str(item_price[item]))
    print(item_description[item])
    
    
    quantity=int(input("Quantity: "))
    if quantity!=0:
        item_quantity.append(quantity)
        cart_items.append(item)
        
    print("1 - Continue Shopping")
    print("2 - View Cart")
    continue_shopping=input("")

print("--------------------")
print("CART")
print("--------------------")
print("ID \tName\t\t\t\tPrice\t\tQuantity")
for i in range(len(cart_items)):
    print(item_id[cart_items[i]], end='\t')
    print(item_name[cart_items[i]], end='\t\t\t')
    print("P"+str(item_price[cart_items[i]]), end='\t\t')
    print(item_quantity[i])
    
    cart_total += (item_price[cart_items[i]]*item_quantity[i])
    
print("Total: P"+str(cart_total))