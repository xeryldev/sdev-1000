# funnyFaces.py
# Smiley face drawing code for you to repair.

# Note we are importing a special, enhanced version of 
# Zelle's grahpics library.
from graphicsWithArc import *

def drawFilledCircle(window, centerPoint, radius, fillColor):
  c1 = Circle(centerPoint,radius)
  c1.setFill(fillColor)
  c1.draw(window)

def drawUnfilledArc(window, rectTopLeft, rectBottomRight, extent): 
  arc = Arc(rectTopLeft, rectBottomRight, extent)
  arc.setWidth(3)
  arc.draw(window)
##########################################################################
############### change no code above this line ###########################
##########################################################################

def funnyFace1(window, center):
  radius = 60
  drawFilledCircle(window, center, radius, "yellow")

  centerX = center.getX()
  centerY = center.getY()
  eye1CenterX = centerX - (radius * .4)
  eyeCenterY = centerY - (radius * .25)
  p2 = Point(eye1CenterX, eyeCenterY)
  drawFilledCircle(window, p2, radius*.25, "black")

  eye2CenterX = centerX + (radius * .4)
  eye2CenterY = centerY - (radius * .25)
  p3 = Point(eye2CenterX, eyeCenterY)
  drawFilledCircle(window, p3, radius*.25, "black")

  mouthTopX = centerX - (radius * .4)
  mouthTopY = centerY + (radius * .3)
  mouthBottomX = centerX + (radius * .4)
  mouthBottomY = centerY + 1.5 * (radius * .4)
  mouthTopLeft = Point(mouthTopX, mouthTopY)
  mouthBottomRight = Point(mouthBottomX, mouthBottomY)
  drawUnfilledArc(window, mouthTopLeft, mouthBottomRight, -180)
  
  # funnyFace1's 2nd eye was filled in with yellow instead of black. 
  # I changed the fill color for the second eye to black to fix it.
  # 


def funnyFace2(window, center):
  radius = 60
  drawFilledCircle(window, center, radius, "yellow")
  

  centerX = center.getX()
  centerY = center.getY()
  eye1CenterX = centerX - (radius * .4)
  eyeCenterY = centerY - (radius * .25)
  p2 = Point(eye1CenterX, eyeCenterY)
  drawFilledCircle(window, p2, radius*.25, "black")

  eye2CenterX = centerX + (radius * .4)
  eye2CenterY = centerY - (radius * .25)
  p3 = Point(eye2CenterX, eyeCenterY)
  drawFilledCircle(window, p3, radius*.25, "black")

  mouthTopX = centerX - (radius * .4)
  mouthTopY = centerY + (radius * .3)
  mouthBottomX = centerX + (radius * .4)
  mouthBottomY = centerY + 1.5 * (radius * .4)
  mouthTopLeft = Point(mouthTopX, mouthTopY)
  mouthBottomRight = Point(mouthBottomX, mouthBottomY)
  drawUnfilledArc(window, mouthTopLeft, mouthBottomRight, -180)

  # funnyFace2 had a bug where we couldn't see any of the eyes or the mouth.
  # the problem was that the drawFilledCirlce line was all the way at the bottom, after
  # the drawUnfilledArc line. This resulted in all of the features of the yellow face
  # being hidden under the yellow face.
  # To fix this, I simply moved the drawFilledCircle line to the top, under the radius
  # where it should be.

def funnyFace3(window, center):
  radius = 60
  drawFilledCircle(window, center, radius, "yellow")

  centerX = center.getX()
  centerY = center.getY()
  eye1CenterX = centerX - (radius * .4)
  eyeCenterY = centerY - (radius * .25)
  p2 = Point(eye1CenterX, eyeCenterY)
  drawFilledCircle(window, p2, radius*.25, "black")

  eye2CenterX = centerX + (radius * .4)
  eye2CenterY = centerY - (radius * .25)
  p3 = Point(eye2CenterX, eyeCenterY)
  drawFilledCircle(window, p3, radius*.25, "black")

  mouthTopX = centerX - (radius * .4)
  mouthTopY = centerY + (radius * .3)
  mouthBottomX = centerX + (radius * .4)
  mouthBottomY = centerY + 1.5 * (radius * .4)
  mouthTopLeft = Point(mouthTopX, mouthTopY)
  mouthBottomRight = Point(mouthBottomX, mouthBottomY)
  drawUnfilledArc(window, mouthTopLeft, mouthBottomRight, -180)

  # funnyFace3 had a bug where the smile was turned into a frown. This is because
  # the drawUnfilledArc had a negative value of 180 instead of a positive value of 180.
  # I simply deleted the negative character before 180 to turn it into a smile. 
  # that's one way to turn a frown upside down!

##########################################################################
############### change no code below this line ###########################
##########################################################################
def main():
  print('Welcome to a world of funny faces!')
  print()
  
  win = GraphWin("Funny Face", 400, 800)
  # For on-screen text, we use a point to define the center spot
  message = Text(Point(200, 25), "Click anywhere to quit")
  message.draw(win)

  # draw the various faces
  p1 = Point(200, 100)
  funnyFace1(win, p1)

  p2 = Point(200, 250)
  funnyFace2(win, p2)
 
  p3 = Point(200, 400)
  funnyFace3(win, p3)

  # wait for click and then quit
  win.getMouse()
  win.close()


main()