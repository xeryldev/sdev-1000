# stringSong.py
# Code to generate some simple lyrics from a variety of variables
#
def main():
  # To help you slice actors more easily, I provide an indexing guide
  #                   1         2         3         4
  #         01234567890123456789012345678901234567890123456
  actors = "drummerslordsmaidsgeesecalling birdsturtle doves"
  placeholder1 = "*"
  placeholder2 = '#'
  placeholder3 = '+'

  print('#' * 20)

  ############ examples, do not change code between these lines ###########
  # On the 12th day of Christmas
  firstLine = "On the 12th day of Christmas"
  print(firstLine)

  # My true love gave to me
  linePart1 = "My true love"
  linePart2 = "gave to me"
  print(linePart1, linePart2)

  # 12 drummers drumming
  stringCount = "12"
  actor = actors[0:8]
  action = "drumming"
  print(stringCount, actor, action)

  # 11 pipers piping
  count = 11
  actor = "pipers"
  action = "piping"
  wholeLine = str(count) + " " + actor + " " +action
  print(wholeLine)
  ############ examples, do not change code between these lines ###########

  # 10 lords a leaping
  # TODO: change the next line to pull 'lords' out of the actors string
  actor = "lords"
  linePart1 = "10 " + actor
  linePart2 = "a leaping"
  print(linePart1, linePart2)  # don't change this line

  # 9 ladies dancing
  count = str(9)
  # TODO: use a function call and concatenation (+) to assemble the correct linePart1
  linePart1 = count + " " + "ladies"
  linePart2 = "dancing"
  print(linePart1, linePart2)  # don't change this line

  # 8 maids a milking
  stringCount = "8"
  # TODO: change the next line to pull 'maids' out of the actors string
  actor = "maids"
  # TODO change the next line to assign the right string to action
  action = "a milking"
  print(stringCount, actor, action)  # don't change this line
  
  # 7 swans a swimming
  count = str(7)  # don't change this line
  # TODO: change the placeholder side of each of the next three lines
  stringCount = count  # replace with a function call
  actor = "swans"		  # replace with a string
  action =  "swimming"     # replace with a string
  wholeLine = stringCount + " " + actor + " " + action # don't change this line
  print(wholeLine)  # don't change this line
  
  # 6 geese a laying
  # TODO: change the next line to pull 'geese' out of the actors string
  actor = "geese"
  linePart1 = "6 " + actor
  linePart2 = "a laying"
  print(linePart1, linePart2)  # don't change this line
  
  # 5 golden rings
  # TODO: assign the correct string values to these 2 variables
  stringCount = str(5)
  actor = "golden rings!"
  print(stringCount, actor)  # don't change this line
  
  # 4 calling birds
  count = 4  # don't change this line
  # TODO: change the next line to pull 'calling birds' out of the actors string
  actor = "calling birds"
  # TODO replace the placeholders with code that assembles the calling birds line
  wholeLine = str(count) + " " + actor
  print(wholeLine)  # don't change this line
  
  # 3 French hens
  # TODO: replace the two placeholder variables with two hard-coded strings
  # (see true love example above)
  linePart1 = "3 "
  linePart2 = "french hens"
  wholeLine = linePart1 + linePart2   # don't change this line
  print(wholeLine)  # don't change this line
  
  # 2 turtle doves
  # TODO: change the next line to pull 'turtle doves' out of the actors string
  actor = actors[36:48]
  wholeLine = "2 " + actor # don't change this line
  print(wholeLine)  # don't change this line

  # And a partridge in a pear tree
  lastLine = "And a partridge in a pear tree!"
  print(lastLine)
  print('#' * 20)

main()