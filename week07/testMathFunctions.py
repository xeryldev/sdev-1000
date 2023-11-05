from mathFunctions import *
import unittest

##################################################
###  DO NOT CHANGE THE CODE IN THIS FILE       ###
##################################################
class TestSimpleFunctions(unittest.TestCase):

  def test_double(self):
    self.assertEqual(double(0),0)
    self.assertEqual(double(1),2)
    self.assertEqual(double(-100),-200)

  def test_square(self):
    self.assertEqual(square(1),1)
    self.assertEqual(square(10),100)
    self.assertEqual(square(-10),100)

  def test_perimeterOfRectangle(self):
    self.assertEqual(perimeterOfRectangle(3, 5),16)
    self.assertEqual(perimeterOfRectangle(10, 10),40)
    self.assertEqual(perimeterOfRectangle(20, 30),100)
 
  def test_areaOfRectangle(self):
    self.assertEqual(areaOfRectangle(3, 5),15)
    self.assertEqual(areaOfRectangle(10, 10),100)
    self.assertEqual(areaOfRectangle(20, 30),600)

  def test_perimeterOfTriangle(self):
    self.assertEqual(perimeterOfTriangle(0,0,0),0)
    self.assertEqual(perimeterOfTriangle(1,2,3),6)
    self.assertEqual(perimeterOfTriangle(3,5,8),16)
 
  def test_areaOfTriangle(self):
    self.assertEqual(areaOfTriangle(0,0),0)
    self.assertEqual(areaOfTriangle(1,2),1)
    self.assertEqual(areaOfTriangle(3,5),7.5)
    
  def test_perimeterOfCircle(self):
    self.assertAlmostEqual(perimeterOfCircle(0), 0, 2)
    self.assertAlmostEqual(perimeterOfCircle(1), 6.28, 2)
    self.assertAlmostEqual(perimeterOfCircle(4), 25.13, 2)
 
  def test_areaOfCircle(self):
    self.assertAlmostEqual(areaOfCircle(0), 0, 2)
    self.assertAlmostEqual(areaOfCircle(1), 3.14, 2)
    self.assertAlmostEqual(areaOfCircle(3), 28.27, 2)

# If this file is executed from the commandline,
# unittest.main() will be called.
# If this code is imported, it will not be called.
if __name__ == '__main__':
    unittest.main()