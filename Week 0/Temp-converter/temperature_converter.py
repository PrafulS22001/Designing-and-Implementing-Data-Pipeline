##############################
#Filename: temperature_converter.py
#Date of Code: 17th Jan 2026
#Author: Praful Sharma
##############################

class TemperatureConverter: 
    def __init__(self) -> None:
        """
        initializie the temp to 0
        """
        self.__temperature = 0.0
        
        
    def setTemperature(self, temp:float) -> None: 
        """
        Docstring for setTemperature
        
        :param temp: Description
        :type temp: float
        """
        self.__temperature = temp
        
    def toCelsius(self) -> float:
        """
        Docstring for toCelsius
        
        :param self: Description
        :return: Description
        :rtype: float
        """
        return self.__temperature     
    def toFahrenheit(self) -> float: 
        """
        Docstring for toCelsius
        
        :param self: Description
        :return: Description
        :rtype: float
        """
        return (self.__temperature * (9/5)) + 32
    
    def toKelvin(self) -> float:
        """
        Docstring for toKelvin
        
        :param self: Description
        :param temp: Description
        :return: Description
        :rtype: float
        """
        return self.__temperature + 273.15