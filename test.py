import unittest
from birdgame import update_score

class ClosestTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(update_score(1,0), 1)
    def test_2(self):
        self.assertEqual(update_score(1,5), 5)
    def test_3(self):
        self.assertEqual(update_score(3,3), 3)
