##############################
#Filename: coin_acceptor.py
#Date of Code: 17th Jan 2026
#Author: Praful Sharma
##############################

class CoinAcceptor: 
    def __init__(self) -> None:
        """
        Docstring for __init__
        
        :param self: 
        Initializing the amount to 0
        """
        self.__amount:int = 0  
        self.__value:float = 0.0
    
    def insertCoin(self) -> None:
        self.__amount += 1 
        
    def getAmount(self) -> int:
        return self.__amount 
    
    def getValue(self) -> float:
        return self.__value
    
    def addValue(self, coin_value: float) -> None:
        self.__value += coin_value
    
    def returnCoins(self) -> tuple[int, float]: 
        final_amount = self.__amount
        final_value = self.__value
        self.__amount = 0
        self.__value = 0.0
        return final_amount, final_value