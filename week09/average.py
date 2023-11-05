# average.py
# 
# This script reads a list of students and their grades and outputs
# the students name and average grade.
#
# This code gives you a chance to practice:
# - working with functions
# - reading files
# - working with lists

# TODO: For each comment below that begins with ? -, provide
# a description of what is happening in the next statement.

def average(gradeList):
  # Calculate the sum of all grades in the gradeList
  # TODO: Add the code here to compute the average of the grades provided in gradeList
  total = sum(gradeList)
  if len(gradeList) > 0:
    avg = total / len(gradeList)
  else:
    avg = 0
  return avg

def main():
  # ? - store the file pointer for the file students.txt in the variable
  # infile.
  infile = open("students.txt")
  for line in infile:
    # ? - The following line is removing the carriage return. The carriage
    # return would causes issues when we call split below.
    line = line[:-1]
    # ? - The following line is creating a list from the line just 
    # read and assigning that list to the variable lineList.  We are doing this
    # because we need to break the line into pieces.  Some of the pieces are the 
    # grades and one piece is the name of the student.
    lineList = line.split(' ')
    # ? - this function takes each line from
    # students.txt and splits each item 
    # that is separated by a space character
    itemCount = 0
    # ? - this sets up the variable that will count each of our grades which we will
    # then use the count of to determine the
    # average of each student's grade
    grades = []
    # ? - this sets up the grades variable
    # where we will store the data for each
    # students' grades that we will collect
    # and turn into an average
    name   = ''
    # ? - this stores the name of each student
    # that we will print out at the end for
    # each average that we collect
    for lineItem in lineList:
      # ? - this sets up our for function 
      # that will allow us to add to the 
      # count of each item and adds the
      # students name from each set of numbers
      itemCount = itemCount + 1
      # ? - this counts each item in the set
      # of a strudents' set of grades.
      if (itemCount == 1):
        name = lineItem
      else:
        # ? - this is how we collect the 
        # name of the student that we are 
        # collecting the averages from, 
        # because the first item in each 
        # list is the name of the student.
        grades.append(int(lineItem))

    # ? - this adds each integer grade in 
    # the set to our grades that we will 
    # use to calculate the average.
    averageGrade = average(grades)
    averageGrade = round(averageGrade, 2)
    print(name + ' has an average grade of: ' + str(averageGrade))

  # ? - this tells the program to execute 
  # our average function based on the grades
  # we have collected, and then prints the 
  # average along with the student's name 
  # and the 'has an average grade of:' part
  infile.close()

main()