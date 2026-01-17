##############################
#Filename: main.py
#Date of Code: 15th Jan 2026
#Author: Praful Sharma
##############################
from Counter import counter

def option(): 
    print()
    print("Options:")
    print("1) Add count")
    print("2) Get count")
    print("3) Zero count")
    print("0) Exit program")
    return None 

def main(): 
    print("Program starting.")
    print("Initializin counter...")
    Counter = counter() #crucial cuz this line tells the program that the counter is present and actually initializes the counter
    print("Counter Initialized.")
    while True: 
        option()
        choice = input("Choice: ")
        if choice == "1":
            Counter.addCount()
            print("Count increased")
        elif choice == "2": 
            print (f"Current count '{Counter.getCount()}'")
        elif choice == "3": 
            Counter.zeroCount()
            print("Count zeroed")
        elif choice == "0": 
            break
        else: 
            print ("Invalid error!")
    
    print("Program ending.")
    return None

if __name__ == "__main__":  
    main()