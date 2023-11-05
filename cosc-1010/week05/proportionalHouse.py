# proportionalHouse.py
# Draw a house in the Python graphics window
# It should "sit" at the bottom/middle of any size
# window and the various elements should be located 
# with numerical expressions so that they are proportional
# to the house as it resizes.

from graphics import *

def main():
  # We should be able to change the dimensions in the following
  # statement and see the house re-size itself to sit on the 
  # bottom of the new window. All components should resize to 
  # suit the new size of the frame
  win = GraphWin("Build a House", 600, 400)

  graphWinWidth = win.getWidth()
  graphWinHeight = win.getHeight()
  print("current GraphWin window is", graphWinWidth, "wide by", graphWinHeight, "high")

  # Center the text in the window, no matter what width it is
  message = Text(Point(graphWinWidth/2,20),"")
  message.draw(win)
  message.setText("This is Steven's house")

  # Set up values here that we will use below to size and locate
  # the shapes that make up the picture of the house.
  # Note: You MAY change the proportions of your overall house
  # and its door here, but do not eliminate any of these variables
  houseWidth = graphWinWidth * .6
  houseHeight = graphWinHeight * .6
  houseOffset = (graphWinWidth - houseWidth) / 2    # center the house left to right
  doorWidth = houseWidth / 3
  doorOffsetFromLeft = doorWidth / 2  
  doorHeight = doorWidth * 2

  # Note: You probably need at least the following three variables to create 
  # the resizable window and door
  windowSize = doorWidth / 2 # if window is square, height == width
  windowOffset = windowSize / 2
  roofHeight = 2

  frameColor = "white"
  doorColor = "blue"
  windowColor = "teal"
  roofColor = "green"

  ########## do not change the code between these two comments ###########
  # Draw the frame of the house
  # It sits on the "floor" of the Window, graphWinHeight pixels down
  frameLowerLeft = Point(houseOffset, graphWinHeight)  
  # Note that, to move up on the canvas, we SUBTRACT from the y value of the bottom edge
  frameUpperRight = Point(frameLowerLeft.getX()+houseWidth, graphWinHeight-houseHeight)
  frame = Rectangle(frameLowerLeft, frameUpperRight)
  frame.setFill(frameColor)
  frame.draw(win)

  # Draw a door
  doorLowerLeft = Point(frameLowerLeft.getX()+doorOffsetFromLeft, graphWinHeight)
  doorUpperRight = Point(doorLowerLeft.getX()+doorWidth, graphWinHeight-doorHeight)
  door = Rectangle(doorLowerLeft, doorUpperRight)
  door.setFill(doorColor)
  door.draw(win)
  ########## do not change the code between these two comments ###########

  # TODO: Draw a window
  windowUpperRight = Point(frameUpperRight.getX()-windowOffset, doorUpperRight.getY())
  windowLowerLeft = Point(doorUpperRight.getX()+doorOffsetFromLeft, doorUpperRight.getY()+windowSize)
  window = Rectangle(windowLowerLeft, windowUpperRight)
  window.setFill(windowColor)
  window.draw(win)
  
  # TODO: Draw the roof
  roof1 = Point(frameLowerLeft.getX(),frameUpperRight.getY())
  roof2 = Point(doorUpperRight.getX(),frameUpperRight.getY()/roofHeight)
  roof3 = Point(frameUpperRight.getX(),frameUpperRight.getY())
  roof = Polygon(roof1, roof2, roof3)
  roof.setFill(roofColor)
  roof.draw(win)
  
  win.getMouse()
  win.close()

main()
    
    
    
    