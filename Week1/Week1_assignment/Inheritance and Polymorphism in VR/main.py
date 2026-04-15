##############################
# Filename: main.py
# Date of Code: 11th April 2026
# Author: Praful Sharma
##############################

from entity_model import *

def add_entity():
    print ("\n Choose entity type:")
    print (" 1 - Player")
    print (" 2 - NPC")
    print (" 3 - Object")

    choice = input("Enter choice: ")

    name = input ("Enter name: ")
    x = input ("Enter X position: ")
    y = input ("Enter Y position: ")
    position = (x, y)

    if choice == "1": 
        level = input ("Enter player level: ")
        return Player(name, position, level)
    
    elif choice == "2": 
        dialogue = input ("Enter NPC dialogue: ")
        return NPC(name, position, dialogue)

    elif choice == "3": 
        description = input ("Enter object description: ")
        return Object(name, position, description)
    
    else: 
        print("Invalid choice! Returning to menu.")
        return None
    

def interact_with_entities(entities):
    if not entities: 
        print ("\nNo entities available!")
        return
    
    print ("\n--- Interactions Begin ---")
    for e in entities:
        print(f"\nInteraccting with {e.name} ({e.__class__.__name__})")
        e.interact()
    print("\n--- Interactions End ---")

def main(): 
    entities = []

    while True: 
        print("\n==== MENU ====")
        print("1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1": 
            new_entity = add_entity()
            if new_entity: 
                entities.append(new_entity)
                print(f"{new_entity.__class__.__name__} added successfully!")
            
        elif choice == "2": 
                interact_with_entities(entities)

        elif choice == "3": 
                print ("Exiting program...")
                break

        else: 
                print ("Invalid menu choice! Try again.")

if __name__ == "__main__": 
    main()