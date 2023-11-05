# flags.py
# Program to draw three sovereign flags, at least one of which should be 
# Native American. See your options at:
#   https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags
#   https://commons.wikimedia.org/wiki/Flags_of_Native_Americans_in_the_United_States

from graphics import *

def main():
  print('Hello Flag Enthusiasts!')
  print()
  
  # TODO: Change the output to show your name
  win = GraphWin("Steven's Flags", 400, 600)
  
  # For on-screen text, note that we use a point to define the CENTER
  # of the text
  message = Text(Point(200, 25), "Click anywhere to quit")
  message.draw(win)
  
  # Graphwin allows many colors to be specified by name, Zelle Section 4.8.5, page 121.
  # See https://www.w3schools.com/colors/colors_x11.asp for a complete list.
  # But some of the simpler HTML/CSS color names (blue, red) work fine also.
  # Colors may also be specified with six-digit hex numbers, as in
  # #ff0000 for red, #00ff00 for green, #0000ff for blue
  
  # All flags should be 300 wide, 200 high
  
  ############### Flag of XXXX ####################
  # TODO: print one or two lines with a description of your flag or
  # of what it symbolizes
  print("The flag of Japan is a red circle on a white rectangle")
  print("It is said to embody the country's nickname: 'The Land of the rising sun'")
  print()

  # TODO: draw your first flag
  # Create two point objects to define the upper-left and lower-right
  # dimensions of white rectangle. Then draw the rectangle.
  p1 = Point(50, 50)
  p2 = Point(180, 140)
  r1 = Rectangle(p1, p2)
  r1.setFill("white")
  r1.draw(win)
  
  # Create a point object to define the center of the red circle,
  # Then, draw the circle.
  p3 = Point(115, 95)
  c1 = Circle(p3, 20)
  c1.setFill("red")
  c1.draw(win)
  
  message = Text(Point(115, 160), "Japan")
  message.draw(win)
  ####################################################

  p4 = Point(220,50)
  p5 = Point(350,95)
  r2 = Rectangle(p4,p5)
  r2.setFill("blue")
  r2.draw(win)
  p6 = Point(220,95)
  p7 = Point(350,140)
  r3 = Rectangle(p6,p7)
  r3.setFill("yellow")

  message = Text(Point(285,160), "Ukraine")
  message.draw(win)
  r3.draw(win)

  print("The first national flag for Ukraine was adopted in 1848 by revolutionaries who wanted its western parts to be freed from Austro-Hungarian rule. They based their flag, consisting of equal horizontal stripes of yellow over blue, on the colours of the coat of arms used by the city of Lviv.")
  print()

  ##########################################################

  p8 = Point(100,180)
  p9 = Point(200,275)
  r4 = Rectangle(p8,p9)
  r4.setFill("orange")
  r4.draw(win)
  p10 = Point(200,180)
  p11 = Point(300,275)
  r5 = Rectangle(p10,p11)
  r5.setFill("green")
  r5.draw(win)
  p12 = Point(200,230)
  r6 = Circle(p12, 15)
  r6.setFill("yellow")
  r6.draw(win)
  p13 = Point(200,230)
  r6 = Circle(p13, 10)
  r6.setFill("white")
  r6.draw(win)

  

  message = Text(Point(200,290), "Niniłchik Village Tribe")
  message.draw(win)
  print("According to the designer, Argent Kvasnikoff 'The overall image of the flag represents a faceted yellow agate stone reflecting direct sunlight on an ocean shore, emblematic of the Niniłchik tribe’s waterways and history.' ")
  print()



  
  win.getMouse()
  win.close()

main()