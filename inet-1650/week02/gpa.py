# gpa.py  
# Code to calculate a grade point average (GPA) from 3 grades

def main():
  print("This program will calculate a GPA from 5 letter grades")
  print("Enter letter grades: A, B, C, D, or F")
  print("Sorry, no plus or minus grades are currently supported.")
  print()

  sum = 0
  for i in range(5):
    gradeValue = getGradeNumericValue()
    sum = sum + gradeValue

  gpa = sum / 5

  print()
  print("The grade point average is: ", gpa)

def getGradeNumericValue():
  value = -1
  gradeLetter = input("Enter one letter grade: ")
  gradeLetter = gradeLetter.upper()

  # We will loop until user gives us a valid letter grade
  while value == -1:
    if gradeLetter == 'A':
      value = 4
    elif gradeLetter == 'B':
      value = 3
    elif gradeLetter == 'C':
      value = 2
    elif gradeLetter == 'D':
      value = 1
    elif gradeLetter == 'F':
      value = 0
    else:
      # If we don't get a valid letter, don't change the starting value,
      # instead, let the user know they made an error and give them another chance.
      gradeLetter = input("***Error: The letter grade must be an A, B, C, D, or E. Please try again: ")
      gradeLetter = gradeLetter.upper()

  return value
  
main()