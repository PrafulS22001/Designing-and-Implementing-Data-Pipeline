##############################
#Filename: char_model.py
#Date of Code: 11th March 2026
#Author: Praful Sharma
##############################

class GameCharacter(): 
    __attack : str
    __defend : str
    def __init__ (self, __attack, __defend): 
        self.__attack = __attack
        self.__defend = __defend
        
    def attack(self): 
        print(self.__attack)
        
    def defend(self): 
        print(self.__defend)

class Warrior(GameCharacter): 
    def __init__(self) -> None:
        super().__init__("CHING", "HAH!!")
        return None

class Mage(GameCharacter):
    def __init__(self) -> None:
        super().__init__("AVADAKADABRA", "PROTEGO!")
        return None

class Archer(GameCharacter): 
    def __init__(self) -> None:
        super().__init__("DRAWW", "DUCK")
        
