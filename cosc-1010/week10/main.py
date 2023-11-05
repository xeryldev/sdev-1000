# houseDraw.py

from graphics import *

def drawGridLines(win):
  maxX = win.getWidth()
  maxY = win.getHeight()
  # vertical lines
  for x in range(10, maxX, 10):
    line = Line(Point(x,0), Point(x,maxY))
    line.setOutline('lightgray')
    line.draw(win)
  # horizontal lines
  for y in range(10, maxY, 10):      
    line = Line(Point(0,y), Point(maxX,y))
    line.setOutline('lightgray')
    line.draw(win)

def getColor(colorLetter):
  # Do not change next two lines
  letters = ['r','o','y','g','b','i','v', 'p', 'c']
  colors  = ['red','orange','yellow','green','blue','indigo','violet', 'pink', 'cyan']

  if colorLetter in letters:
    return colors[letters.index(colorLetter)]
  else:
    return "black"
  
def drawHouse(win, frameLowerLeft, frameUpperRight, frameColor, doorColor, chimneyPos, roofColor, windowColor):
  # Do not change following three statements
  houseWidth = frameUpperRight.getX() - frameLowerLeft.getX() 
  houseHeight = frameLowerLeft.getY() - frameUpperRight.getY()
  print("House is", houseWidth, "wide and", houseHeight, "high")

  #doorWidth is 1/3 of the houseWidth
  doorWidth = houseWidth / 3
  #doorOffsetFromLeft is 1/2 of doorWidth
  doorOffsetFromLeft = doorWidth / 2  
  #doorHeigth is 60% of houseHeight
  doorHeight = houseHeight * 0.6

  #roofHeight is 20% of houseHeight
  roofHeight = houseHeight * 0.2

  # Add code below to define a windows that has width and height 
  # that are 25% of the house width and height respectively.
  # The window shold be centered between the doors right edge
  # and the right edge of the house

  windowWidth = houseWidth * 0.25
  windowHeight = houseHeight * 0.25
  windowOffsetX = (doorOffsetFromLeft + doorWidth) + (houseWidth - (doorOffsetFromLeft + doorWidth + windowWidth)) / 2

  frame = Rectangle(frameLowerLeft, frameUpperRight)
  frame.setFill(frameColor)
  frame.draw(win)

  # Draw a door
  doorLowerLeft = Point(frameLowerLeft.getX()+doorOffsetFromLeft, frameLowerLeft.getY())
  doorUpperRight = Point(doorLowerLeft.getX()+doorWidth, frameLowerLeft.getY()-doorHeight)
  door = Rectangle(doorLowerLeft, doorUpperRight)
  door.setFill(doorColor)
  door.draw(win)

  #Draw a chimney. Add code below.
  chimneyOffset = houseWidth * .05
  chimneyWidth = doorWidth / 2

  if chimneyPos == 'cr':
    chimneyUpperRight = Point(frameUpperRight.getX() - chimneyOffset, frameUpperRight.getY() - roofHeight)
    chimneyLowerLeft = Point(chimneyUpperRight.getX() - chimneyWidth, frameUpperRight.getY())
  elif chimneyPos == 'cl':
    chimneyLowerLeft = Point(frameLowerLeft.getX() + chimneyOffset, frameUpperRight.getY())
    chimneyUpperRight = Point(chimneyLowerLeft.getX() + chimneyWidth,frameUpperRight.getY() - roofHeight)
  else:
    print("incorrect chimney positional value!")
  # drawing chimney shape
  print(chimneyLowerLeft, chimneyUpperRight)
  chimney = Rectangle(chimneyLowerLeft, chimneyUpperRight)
  chimney.setFill(getColor('bl'))
  chimney.draw(win)
  
  # Draw the roof. Add your code below.
  roofLeft = Point(frameLowerLeft.getX(), frameUpperRight.getY())
  roofTop = Point(doorUpperRight.getX(), frameUpperRight.getY() - roofHeight)
  roof = Polygon(roofLeft, roofTop, frameUpperRight)
  roof.setFill(roofColor)
  roof.draw(win)

  # Draw a window. Add your code below.
  windowOffsetX = (houseWidth - doorWidth - doorOffsetFromLeft - windowWidth) / 2
  windowUpperRight = Point(doorUpperRight.getX() + windowOffsetX + windowWidth, doorUpperRight.getY())
  windowLowerLeft = Point(doorUpperRight.getX() + windowOffsetX, windowUpperRight.getY() + windowHeight)
  window = Rectangle(windowLowerLeft, windowUpperRight)
  window.setFill(windowColor)
  window.draw(win)

def main():
  win = GraphWin("My Rainbow Street", 600, 600)
  win.setBackground("white")

  drawGridLines(win)

  # The file rainbowHouses.txt contains a description of a house per line.
  # The first two numbers represent the lower left position of the house.
  # The second two numbers represent the upper right position of the house.
  # The next 3 letters represent the color of the frame, door, and roof.
  infile = open("rainbowHouses.txt")
  for line in infile:
    # remove the linefeed at the end of each line

    # Add your code after these comments to create the lowerLeft 
    # corner of the house (frameLowerLeft)
    # as a Point, the upperRight corner of the house (frameUpperRight) as a Point
    # and the variables to hold the three colors frameColor, doorColor, and roofColor

    houseParams = line.strip().split(', ')
    frameLowerLeft = Point(float(houseParams[0]), float(houseParams[1]))
    frameUpperRight = Point(float(houseParams[2]), float(houseParams[3]))
    frameColor = getColor(houseParams[4])
    doorColor = getColor(houseParams[5])
    chimneyPos = houseParams[-1]
    roofColor = getColor(houseParams[6])
    windowColor = getColor(houseParams[-2])
    
    # once all variables created, drawHouse (do not change the next statement)
    drawHouse(win, frameLowerLeft, frameUpperRight, frameColor, doorColor, chimneyPos, roofColor, windowColor)

  infile.close()
  # Do not delete the following statements
  win.getMouse()
  win.close()
  # No code is required below this line
  
main()