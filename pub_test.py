import unittest
from pub import Pub
from drink import Drink
from customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.beer = Drink("Innis & Gunn", 5)
        self.whiskey = Drink("Old Fashioned", 12)
        self.drinks = [self.beer, self.whiskey]
        self.customer = Customer("Holly", 50)
        self.pub = Pub("The Three Broomsticks",1000, self.drinks)

    def test_sell_drink(self):
        self.pub.sell_drink(self.beer, self.customer)
        self.assertEqual(1005,self.pub.till)
        self.assertEqual(45, self.customer.wallet)