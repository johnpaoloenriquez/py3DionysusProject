"""Planned system for menu:
    - the menu will be read from a file like an excel or a txt file
    - the code should read item prices, item name, item decscription and item id
    - if creating a dynamic menu from excel is not possible then, use lists or numpy arrays instead to display the menu
"""
import openpyxl

#read excel using openpyxl
# the excel file can be placed in the cloud to make it accessible anywhere, or it can be placed in the same folder as the python file
dataframe = openpyxl.load_workbook('itemlist.xlsx')
dataframe1 = dataframe.active

# Iterate the loop to read the cell values
# 1st argument is the row number

item_id=[]
item_name=[]
item_price=[]
item_description=[]

#Get the item name id
for col in dataframe1.iter_cols(1, 1):
    #print(row)
    
    for row in range(1, dataframe1.max_row): 
        a=col[row].value
        item_id.append(a)



#get the item name
for col in dataframe1.iter_cols(2, 2):

    
    for row in range(1, dataframe1.max_row): 
        a=col[row].value
        item_name.append(a)
    
#get the item price    
for col in dataframe1.iter_cols(3, 3):

    
    for row in range(1, dataframe1.max_row): 
        a=col[row].value
        item_price.append(a)
    
#Get the item description   
for col in dataframe1.iter_cols(4, 4):
    #print(row)
    
    for row in range(1, dataframe1.max_row): 
        #print(col[row].value)
        a=col[row].value
        item_description.append(a)