# if testing code you need to do the 2-3 steps
import unittest
from checker_file import do_stuff
# To make it work, you need a class that test the method and test concept that call unittest
class HoldFunc(unittest.TestCase):
	def setUp(self):
		print("this can stand as default, and start any test")
	def test_do_stuff(self): # function that test result of the real code file
		'''compare to make a like'''
		num = 10
		result = do_stuff(num) # checker method using assertEqual
		self.assertEqual(result, 15)

	def test_do_stuff2(self):
		word = "dahajf"
		result = do_stuff(word) # also this, but in error form
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		wrong = None
		result = do_stuff(wrong)
		self.assertEqual(result, "please enter number")
	
	def tearDown(self):
		print("this can be seen as end root and also end any test")

if __name__ == "__main__":
	unittest.main() # call by using the main tester file (like: checker_file.py)
