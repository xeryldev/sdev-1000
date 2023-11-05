# speeding.py
# this program will calculate the speeding ticket fines for Podunkville
# speeding ticket fine policy is 5x + 50 ($50, and 5$ more for each mph over the limit)
# if the clocked speed is over 90, add additional fine of $200 (90 >= 5x + 50 + 200)
def main():
  limit = int(input("What is the current speed limit?: "))
  speed = int(input("What is the current clocked speed?: "))
  fine = speed * 5 + 50
  if speed <= limit:
    print("this speed is legal to drive.")
  elif limit >= 90:
    fine = speed * 5 + 50 + 200
    print("this speed is illegal to drive, and you are driving over 90 mph.")
    print("you will have to pay an additional $200, therefore your fine will be $", fine)
  else:
    print("this speed is illegal to drive! you will have to pay a fine of $", fine)
main()