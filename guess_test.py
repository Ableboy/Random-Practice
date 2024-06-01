import unittest
from guess_game import guesses_game

class TestGame(unittest.TestCase):
	def tester(self):
		result = guesses_game(5, 5)
		self.assertTrue(True)

if __name__ == "__main__":
	unittest.main()

		