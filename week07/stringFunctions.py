# stringFunctions.py
# This code gives you a chance to practice:
# - reading comments and code
# - reading and writing functions
# Code to run each function appears in main() at the very bottom of this file.
# Be sure to use testStringFunctions.py to verify your code is working correctly

# username1 -- given first and last names, compose username as follows:
# - first letter of the first name, lower-cased
# - up to five letters from the start of the last name, lower-cased
# - Given input: ("Win", "Le"), ("Susie", "McElligott"), ("Clayton", "Danks")
# - Expected output: wle, smcell, cdanks
def username1(first, last):
  name = first[0:1].lower() + last[0:5].lower()
  username = name
  return username

# username2 -- given first and last names, compose username as follows:
# - first letter of the first name, lower-cased
# - up to five letters from the start of the last name, lower-cased
# - last letter of the last name, lower-cased
# - Given input: ("Win", "Le"), ("Susie", "McElligott"), ("Clayton", "Danks")
# - Expected output: wlee, smcellt, cdankss
def username2(first, last):
  name2 = first[0:1].lower() + last[0:5].lower() + last[-1]
  username = name2
  return username

def exerciseStringFunctions():
  # call each function once, display output
  firstName = "Win"
  lastName = "Le"
  username = username1(firstName, lastName)
  username3 = username2(firstName, lastName)
  print()
  print("username #1 for", firstName, lastName, "is: ", username)
  print("username #2 for", firstName, lastName, "is: ", username3)

  firstName = "Susie"
  lastName = "McElligott"
  username = username1(firstName, lastName)
  username3 = username2(firstName, lastName)
  print("username #1 for", firstName, lastName, "is: ", username)
  print("username #2 for", firstName, lastName, "is: ", username3)
  firstName = "Clayton"
  lastName = "Danks"
  username = username1(firstName, lastName)
  username3 = username2(firstName, lastName)
  print("username #1 for", firstName, lastName, "is: ", username)
  print("username #2 for", firstName, lastName, "is: ", username3)

# If this file is executed from the commandline,
# exerciseStringFunctions() will be called.
# If this code is imported, it will not be called.
if __name__ == '__main__':
  exerciseStringFunctions()
