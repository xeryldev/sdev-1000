# exploreRounding.py
# Calculate dozens for sellers and buyers of eggs
# using floor() and ceil() from the math library

import math

def main():

  print("This program will calculate dozens for eggs to buy and sell.")
  print()
  numberOfEggs = int(input("Enter how many eggs you want to sell/buy: "))

  print("Seller has", numberOfEggs, "eggs")
  sellerDozen = math.floor(numberOfEggs/12)
  print("Seller can sell", sellerDozen, "dozen.")
  print()
  
  print("Buyer needs", numberOfEggs, "eggs") 
  buyerDozen = math.ceil(numberOfEggs/12)
  print("Buyer must purchase", buyerDozen, "dozen.")

main()