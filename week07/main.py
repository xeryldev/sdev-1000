## Driver for all the non-test code in this folder

import mathFunctions
import stringFunctions
import singHappy

def main():
  print(20 * '#')
  print()
  print("From mathFunctions.py:")
  print()
  mathFunctions.exerciseMathFunctions()
  print()
  print(20 * '#')
  print("From stringFunctions.py:")
  stringFunctions.exerciseStringFunctions()
  print()
  print(20 * '#')
  print("From singHappy.py:")
  singHappy.exerciseSingHappyFunctions()
  print()
  print(20 * '#')


# If this file is executed from the commandline,
# main() will be called.
# If this code is imported, it will not be called.
if __name__ == '__main__':
  main()