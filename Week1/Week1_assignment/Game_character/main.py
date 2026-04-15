##############################
#Filename: main.py
#Date of Code: 11th March 2026
#Author: Praful Sharma
##############################

from char_model import *

def char_option(): 
    print ("Choose character: ")
    print ("1. Warrior")
    print ("2. Mage")
    print ("3. Archer")

    choice = input ("Enter choice: ")

    if choice == "1": 
        return Warrior()
    elif choice == "2": 
        return Mage()
    elif choice == "3": 
        return Archer()
    else: 
        print ("Invalid choice! Returning.")
        return None

def menu(): 
    print("\n====== Menu ======")
    print("1 - Create Character")
    print("2 - Simulate Battle")
    print("0 - Exit")

def simulate_battle(characters):
    if not characters: 
        print("No characters created yet!")
        return
    print ("\n -- Battle simulation --")
    for char in characters: 
        print (f"\n{char.__class__.__name__} attacks:")
        char.attack()
        print (f"\n{char.__class__.__name__} defends:")
        char.defend()
    print("\n -- Battle Ended --")

    
def main(): 
    print ("Welcome to the Humble gaminng experience. Please enjoy.")
    characters = []

    while True: 
        menu()
        choice = input("Enter choice: ")

        if choice == "1": 
            new_char = char_option()
            if new_char: 
                characters.append(new_char)
                print(f"{new_char.__class__.__name__} created successfully!")
            
        elif choice == "2": 
            simulate_battle(characters)

        elif choice == "0": 
            print("Exiting program...")
            break

        else: 
            print ("Invalid menu choice! Try again.")

if __name__ == "__main__": 
    main()