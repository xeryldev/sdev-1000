# futval.py
#    A program to compute the value of an investment after a 
#    user-specified number of years at a user-specified interest rate.

def main():
  print("This program calculates the future value of an investment.")
  
  principal = eval(input("Enter the initial principal: "))
  apr = eval(input("Enter the apr as a decimal (.1 for 10%): "))
  years = eval(input("Enter the number of years to run the calculation: "))
  
  for i in range(years):
      principal = principal * (1 + apr)
      round(principal, 2)
  
  print("The value in", years, "years is:", principal)

main()
