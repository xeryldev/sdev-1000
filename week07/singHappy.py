# If this file is executed from the commandline,
# exerciseMathFunctions() will be called.
# If this code is imported, it will not be called.

def exerciseSingHappyFunctions():
  print("From singAll:")
  print()

if __name__ == '__main__':
  exerciseSingHappyFunctions()

def happy():
  print("Happy birthday to you!")

def sing(person):
  happy()
  happy()
  print("Happy birthday, dear", person + "!")
  happy()

def singAll():
  sing("Harry")
  print()
  sing("Ron")
  print()
  sing("Hermione")
  print()

singAll()