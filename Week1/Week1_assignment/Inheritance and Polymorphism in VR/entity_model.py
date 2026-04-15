##############################
#Filename: entity_model.py
#Date of Code: 11th March 2026
#Author: Praful Sharma
##############################

class Entity: 
    def __init__ (self, name, position): 
        self.name = name
        self.position = position

    def interact(self): 
        raise NotImplementedError ("Subclasses must implement interact()")
    
class Player(Entity): 
    def __init__(self, name, position, level): 
        super().__init__(name, position)
        self.level = level

    def interact(self): 
        print(f"{self.name} (Player) swings a sword at level {self.level}")

class NPC(Entity): 
    def __init__ (self, name, position, dialogue): 
        super().__init__(name, position)
        self.dialogue = dialogue

    def interact(self): 
        print(f"{self.name} (NPC) says: '{self.dialogue}'")

class Object (Entity): 
    def __init__ (self, name, position, description): 
        super().__init__(name, position)
        self.description = description
    
    def interact(self): 
        print(f"{self.name} (Object) is examined: {self.description}")