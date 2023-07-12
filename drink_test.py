import unittest
from drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.beer = Drink("Innis & Gunn", 5)
        self.whiskey = Drink("Old Fashioned", 12)
        self.drinks = [self.beer, self.whiskey]