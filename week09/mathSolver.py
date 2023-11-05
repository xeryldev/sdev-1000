# mathSolver.py
# 
# This script reads a list of math problems from the file mathProblems.txt
# and outputs the result of the math problem.
# 
# You will use your mathFunctions.py file from week07.  Please copy that file 
# into this directory and make sure it is named mathFunctions.py and
# has no main() function.
#
# This code gives you a chance to practice:
# - working with functions
# - reading files
# - working with lists
# - working with if statements

from mathFunctions import *

def main():
  infile = open("mathProblems.txt")
  for line in infile:
    result = 0
    line = line[:-1] # remove the newline character
    # split the line
    components = line.split()
    operation = components[0]
    # get the first item as the operation
    # Using if statements determine what math funtion to call
    # in mathFunctions.py
    # Each if will then convert the items needed into numbers and 
    # call the math function.
    if operation == 'double':
      if len(components) == 2:
          num = float(components[1])
          result = double(num)
    elif operation == 'square':
      if len(components) == 2:
          num = float(components[1])
          result = square(num)
    elif operation == 'rectPerim':
      if len(components) == 3:
          length = float(components[1])
          width = float(components[2])
          result = rectPerim(length, width)
    elif operation == 'rectArea':
      if len(components) == 3:
          length = float(components[1])
          width = float(components[2])
          result = rectArea(length, width)
    elif operation == 'trianglePerim':
      if len(components) == 4:
          side1 = float(components[1])
          side2 = float(components[2])
          side3 = float(components[3])
          result = trianglePerim(side1, side2, side3)
    elif operation == 'triangleArea':
      if len(components) == 3:
          base = float(components[1])
          height = float(components[2])
          result = triangleArea(base, height)
    elif operation == 'circlePerim':
      if len(components) == 2:
          radius = float(components[1])
          result = circlePerim(radius)
    elif operation == 'circleArea':
      if len(components) == 2:
          radius = float(components[1])
          result = circleArea(radius)
    else:
      print("Unsupported operation:", operation)
      continue
      
    # last print the math problem and the result
    # print(theMathProblem + ' = ' + str(result))

    theMathProblem = ' '.join(components)
    print(theMathProblem + ' = ' + str(result))
  

   

  infile.close()

main()