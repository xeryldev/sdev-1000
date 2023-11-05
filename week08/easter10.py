# easter10.py
# this program will calculate the date of easter for any year in the range 1900-2099.
def calcEaster(year):
# this function will use the provided formula to calculate the date of easter using the given year input. 
# if the year is a special year in which the formula will give us the date a week late, we can subtract 7 in order to get an accurate date.
  specialYears = ['1954', '1981', '2049', '2076']
  specialYearGap = 7
  a = year % 19
  b = year % 4
  c = year % 7
  d = (19 * a + 24) % 30
  e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

  if year in specialYears:
    easter = (22 + d + e) - specialYearGap
  else:
    easter = 22 + d + e
  return easter

  
def main():
  year = int(input("Please enter a year: "))

  if (year >= 1900) and (year <= 2099):
    easter = calcEaster(year)
    if easter > 31:
      print("Easter that year is on April {}!".format(easter - 31))
    else:
      print("March {}".format(easter))
  else:
    print("Error: the inputted year is not in the range of 1900-2099!")


if __name__ == '__main__':
  main()