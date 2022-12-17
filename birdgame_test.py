import unittest
from birdgame import update_score


class BirdTests(unittest.TestCase):

    def bird_test_1(self):
        self.assertEqual(update_score(1,0),1)

    def bird_test_2(self):
        self.assertEqual(update_score(1,5),5)

    def bird_test_3(self):
        self.assertEqual(update_score(3,3),3)