##############################
#Filename: main2.py
#Date of Code: 17th Jan 2026
#Author: Praful Sharma
##############################

from temperature_converter import TemperatureConverter

def option(): 
    
    print("Options:")
    print("1) Set temperature")
    print("2) Convert to Celsius")
    print("3) Convert to Fahrenheit")
    print("4) Convert to Kelvin")
    print("0) Exit program")
    return None

def main(): 
    print("Program starting.")
    print("Initializinf temperature converter...")
    TempConvert = TemperatureConverter()
    print("Temperature converter initialized.")
    while True:
        try: 
            option()
            choice = int(input("Choice: ")) 
            if choice == 1: 
                Temp =  float(input("Enter temperature: "))
                TempConvert.setTemperature(Temp)
                print(f"Temperature set to {Temp}")
            elif choice == 2:
                print (f"Temperature in Celsius: {TempConvert.toCelsius()}")
            elif choice == 3: 
                print(f"Temperature in Fahrenheit: {TempConvert.toFahrenheit()}")
            elif choice == 4:
                print(f"Temperature in Kelvin: {TempConvert.toKelvin()}")
            elif choice == 0: 
                break
        except ValueError: 
            raise ValueError ("Invalid input")
    print ("Program ending.")
    return None 

if __name__ == "__main__": 
    main()