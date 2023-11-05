from stringFunctions import *
import unittest

##################################################
###  DO NOT CHANGE THE CODE IN THIS FILE       ###
##################################################
class TestSimpleFunctions(unittest.TestCase):

  def test_username1(self):
    self.assertEqual(username1("Win", "Le"), "wle")
    self.assertEqual(username1("Susie", "McElligott"), "smcell")
    self.assertEqual(username1("Clayton", "Danks"), "cdanks")
    
  def test_username2(self):
    self.assertEqual(username2("Win", "Le"), "wlee")
    self.assertEqual(username2("Susie", "McElligott"), "smcellt")
    self.assertEqual(username2("Clayton", "Danks"), "cdankss")


# If this file is executed from the commandline,
# unittest.main() will be called.
# If this code is imported, it will not be called.
if __name__ == '__main__':
    unittest.main()