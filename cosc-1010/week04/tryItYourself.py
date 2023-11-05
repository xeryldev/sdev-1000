# tryItYourself.py
# Sample graphics code to allow you to practice with the 
# Zelle graphwin objects. Your work in this file will not
# be graded.

from graphics import *

def main():
  # Open a graphics window
  win = GraphWin("Shapes", 600, 600)

  # Draw a red circle centered at point (100, 100) with radius 30
  center = Point(100, 100)
  circ = Circle(center, 30)
  circ.setFill("blue")
  circ.draw(win)

  # Put a text label in the center of the circle
  label1 = Text(center, "Red Cicle")
  label1.draw(win)

  # Draw a square using a Rectangle object
  upperLeft = Point(300, 50)
  lowerRight = Point(400, 150)
  rect = Rectangle(upperLeft, lowerRight)
  rect.setFill("blue")
  rect.draw(win)

  # Put a text label on the screen
  # Note the Point object is being created within the call to
  # create the Text object. It is never assigned to its own variable.
  label2 = Text(Point(150, 200), "Some input label:")
  label2.draw(win)

  # create an input text box
  inputText = Entry(Point(300,200), 5)
  inputText.setText("0.0")
  inputText.draw(win)

  actionText = Text(Point(200, 300),"Poke me!!!!")
  actionText.draw(win)

  # wait for a mouse click, presumably on the button text
  # but we aren't really limiting the user to that
  win.getMouse()

  # Change something on the screen
  actionText.setText("Ouch! That hurt. (Click anywhere to quit.)")
  
  # wait for click and then quit
  win.getMouse()
  win.close()
    
main()
