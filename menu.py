"""Planned system for menu:
    - the menu will be read from a file like an excel or a txt file
    - the code should read item prices, item name, item decscription and item id
    - if creating a dynamic menu from excel is not possible then, use lists or numpy arrays instead to display the menu
"""
import pandas as pd

excel= pd.read_excel('itemlist.xlsx')
print(excel)