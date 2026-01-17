class counter: 
    def __init__ (self): # The underscore makes the variable private so it is not that easy to access from outside the class.
        """
        initializing the count as 0
        """
        self.__count = 0
        
    def addCount(self) -> None: 
        """
        Adding the count/ increasing the count by 1 every single time it is incremented.
        """
        self.__count += 1
    
    def getCount(self) -> int:
        """
        Returning the count
        """
        return self.__count
    
    def zeroCount(self) -> None:
        """
        conveting the value of the count to zero
        """
        self.__count = 0
    
