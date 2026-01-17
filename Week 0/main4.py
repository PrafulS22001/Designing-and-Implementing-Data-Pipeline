##############################
#Filename: main4.py
#Date of Code: 15th Jan 2026
#Author: Praful Sharma
##############################

from coin_acceptor import CoinAcceptor

def main(): 
    print("Program starting.")
    print ("Welcome to coin acceptor program.")
    print ("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    coin = CoinAcceptor()
    while True: 
        try: 
            feed = float (input ("Insert coin(0 return, -1 exit): "))
        except ValueError: 
            print("Invalid input, try again!!")
            continue
        
        if feed == -1:
            print ("Exiting program.")
            break 
        
        elif feed == 0: 
            print ("Returning coins...")
            amount, value = coin.returnCoins()
            print(f"{amount} coins with {value}€ value returned.")
            print (f"Inserted coins = {coin.getAmount()}, value = {coin.getValue()}€")
        
        elif feed > 0: 
            print ("Inserting...")
            coin.insertCoin()
            coin.addValue(feed)
            print(f"Inserted coins = {coin.getAmount()}, value = {coin.getValue()}€")
        
        else:
            print("Number too low, try again.")
    print ("Program ending.")
    return None 

if __name__ == "__main__": 
    main()