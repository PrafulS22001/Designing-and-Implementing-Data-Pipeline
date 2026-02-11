##############################
#Filename: item.py
#Date of Code: 4th Feb 2026
#Author: Praful Sharma
##############################

from dataclasses import dataclass #comes from the standard library module dataclasses. Have to be imported.

@dataclass
class Item: 
    SEPARATOR = ","
    name : str
    value : float
    category : str
    weight : float
    
    # 2 separate decorators, you don't have to use staticmethod AND dataclass; it's either-or
    @staticmethod
    def deserialize(row: str) -> 'Item':
        columns = row.split(Item.SEPARATOR) #Comma seperated values 
        item = Item(
            columns[0], #name
            float(columns[1]), #value
            columns[2],
            float(columns[3]), #weight
        )
        return item

    def display_price(self) -> None:
        print (f"{self.name} costs {self.value} €.")
        return None