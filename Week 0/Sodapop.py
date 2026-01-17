class SodaBoottle: 
    brand = str
    capopen = bool
    
    def __init__ (self, brand, capopen) -> None :
        self.brand = brand
        self.capopen = False
        
    def openBottle (self) -> None: 
        if not self.capopen: 
            print ("sihhhhh")
            self.capopen = True
            
    def drink(self) -> None: 
        if not self.capopen: 
            print ("Can't drink from a closed bottle....")
        else: 
            print (f"Glunk glunk! mmmm.... tastes like {self.brand}.")