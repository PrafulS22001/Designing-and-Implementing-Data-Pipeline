##############################
#Filename: main.py
#Date of Code: 10th Feb 2026
#Author: Praful Sharma
##############################

from file_handler import FileHandler
from item import Item

class Main: 
    def __init__(self) -> None:
        filename = "inventory.csv"
        inventory_file = FileHandler(filename) # Create an object
        rows = inventory_file.read() #Use read method for the previously created object
        items: list[Item] = []
        print("#### inventory ####")
        
        for i in range(len(rows)):
            _item = Item.deserialize(rows[i])
            print(f"{i + 1}. ", end='')
            _item.display_price()
            items.append(_item)
        print("#### inventory ####")
        # allow user to set new item value...
        print ("\n Update the item values: ")
    
        for item in items: 
            new_value = input (f"New value for {item.name} (current{item.value}): ")
            if new_value.strip != "":
                try: 
                    item.set_value(float(new_value))
                except ValueError: 
                    print ("Invalid input")
                    
        print("Serializing items into rows.")
        print("#### rows ####")
        for item in items:
            row = item.serialize()
            print(row)
        print("#### rows ####")
        
if __name__ == "__main__": 
    main = Main()


## ALternative way to do from line 23 
# feed = input(f"Change item value (enter 1- {len(inventory)}): ")
#         try:
#             index = int(feed) - 1
#             feed = input(f"Set new value for {inventory[index].name}: ")
#             inventory[index].set_value(float(feed))
#         except Exception:
#             print("Oops")
#         print("Serializing items into rows")
#         print('## Rows ##')
#         for _item in inventory: 
#             row = item.serialize()
#             print(row)
#         print ("Program ending!")