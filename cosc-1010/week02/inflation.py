# inflation.py
#    This program calculates the future price of an item given
#    the current price, an inflation rate, and a number of years

def main():
  print("This program will calculate the inflation-adjusted price of a product")
  print("over a certain amount of time and rate of inflation.")
  print(" ")
  
  name = input("Enter the name of the product you want to calculate the inflation-adjusted price of: ")
  price = eval(input("Enter the original price of the product: "))
  apr = eval(input("Enter the rate of inflation as a decimal (.1 for 10%): "))
  years = eval(input("Enter the amount of years you want to adjust for: "))

  for i in range(years):
    price = price * (apr + 1)
    price = round(price, 2)
    
  print("The inflation-adjusted price for", name, end = " ")
  print("after", years, end = " ")
  print("years is $", price)
main()

