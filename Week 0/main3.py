##############################
#Filename: main3.py
#Date of Code: 17th Jan 2026
#Author: Praful Sharma
##############################

from coin_acceptor import CoinAcceptor

def option():
    print()
    print("1 - Insert coin")
    print("2 - Show coin")
    print("3 - Return coins")
    print("0 - Exit program")
    return None

def main(): 
    print("Program starting.")
    coin = CoinAcceptor()
    while True: 
        try: 
            option()
            choice = int (input("Your choice: "))
            if choice == 1: 
                coin.insertCoin()
            elif choice == 2: 
                print(f"Currently '{coin.getAmount()}' coins in coin acceptor ")
            elif choice == 3:
                print(f"Coin accpetor returned '{coin.returnCoins()}' coins.")
            elif choice == 0:
                break
        except ValueError: 
            raise ValueError ("Choose a valid choice\n")
    print ("Program ending.")
    return None

if __name__ == "__main__": 
    main()