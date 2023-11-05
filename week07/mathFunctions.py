# mathFunctions.py
# This code gives you a chance to practice:
# - reading comments and code
# - reading and writing functions
# Code to run each function appears in main() at the very bottom of this file.
# Be sure to use testMathFunctions.py to verify your code is working correctly

import math


# double -- given a value, double it and return the result
# Formula: y = 2 * x
# - Given input: 0, 1, 2, 3, 4
# - Expected output: 0, 2, 4, 6. 8
def double(value):
  result = value * 2
  return result


# square -- given a value, calculate its square
# Note: do not use a function from the math libary.
# Formula: y = x * x
# - Given input: 0, 1, 2, 3, 4
# - Expected output: 0, 2, 4, 6. 8
def square(value):
  result = value * value
  return result


# perimeterOfRectangle -- given a length and width, calculate the perimeter of a rectangle.
# Formula: perimeter = side1 * 2 + side2 * 2
# - Given input: (0,0), (1,1), (2,3), (3,5), (5,8)
# - Expected output: 0, 4, 10, 26
def perimeterOfRectangle(length, width):
  result = perimeter = length * 2 + width * 2
  return result


# areaOfRectangle -- given a length and width, calculate the area of a rectangle.
# Formula: area = length# width
# Given input: (0,0), (1,1), (1,2), (2,3), (3,5)
# Expected output: 0, 1, 2, 6, 15
def areaOfRectangle(length, width):
  result = area = length * width
  return result


# perimeterOfTriangle -- given three sides, calculate the perimeter of a triangle.
# Note that this function does not validate that the given triangle can be drawn
# Formula: perimeter = side1 + side2 + side3
# - Given input: (0,0,0), (1,1,1), (1,2,3), (2,3,5), (3,5,8)
# - Expected output: 0, 3, 6, 10, 16
def perimeterOfTriangle(side1, side2, side3):
  perimeter = side1 + side2 + side3
  return perimeter


# areaOfTriangle -- for a given a base and height, calculate the area of a triangle.
# Formula: area = (base# height) / 2
# Reference: https://www.mathsisfun.com/algebra/trig-area-triangle-without-right-angle.html
# - Given input: (0,0), (1,1), (1,2), (2,3), (3,5)
# - Expected output: 0, 0.5, 1, 3, 7.5
def areaOfTriangle(base, height):
  area = (base * height) / 2
  return area


# perimeterOfCircle -- for a given radius, calculate the
#     perimeter (aka circumference) of a circle.
# Formula: perimeter = 2 * pi * radius
# - Given input: 0, 1, 2, 3, 4
# - Expected output: 0, 6.28, 12.56, 18.84, 25.13
#   Note, actual output will have many decimal digits
def perimeterOfCircle(radius):
  perimeter = 2 * math.pi * radius
  result = round(perimeter, 2)
  return result


# areaOfCircle -- for a given a radius, calculate the area of a circle.
# Formula: area = pi * (radius ^ 2)
# use math.pi in place of pi in the formula above
# Given input: 0, 1, 2, 3, 4
# Expected output (rounded to 2 decimal places):  0, 3.14, 12.57, 28.27, 50.27
def areaOfCircle(radius):
  area = math.pi * (radius**2)
  result = round(area, 2)
  return result


def exerciseMathFunctions():
  # call each function once, display output
  x = 10
  y = double(x)
  print("double input:", x, "output:", y)
  print()

  y = square(x)
  print("square input:", x, "output:", y)
  print()

  length = 3
  width = 5
  p = perimeterOfRectangle(length, width)
  print("the perimeter of a rectangle with the length of", length, "and width of", width, "is:", p)
  print()

  a = areaOfRectangle(length, width)
  print("the area of a rectangle with the length of", length, "and width of", width, "is:", a)
  print()

  side1 = 3
  side2 = 4
  side3 = 6
  p = perimeterOfTriangle(side1, side2, side3)
  print("the perimeter of a triangle with the sides", side1, ",", side2, ", and", side3, "is:", p)
  print()

  base = 3
  height = 5
  a = areaOfTriangle(base, height)
  print("the area of a triangle with the base of", base, "and height of", height, "is:", a)
  print()

  radius = 4
  p = perimeterOfCircle(radius)
  print("the perimeter of a circle with the radius of", radius, "is:", p)
  print()

  a = areaOfCircle(radius)
  print("the area of a circle with the radius of", radius, "is:", a)


# If this file is executed from the commandline,
# exerciseMathFunctions() will be called.
# If this code is imported, it will not be called.
if __name__ == '__main__':
  exerciseMathFunctions()
