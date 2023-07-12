import unittest
from customer import Customer
from drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Holly", 50, 27)
        self.beer = Drink("Innis & Gunn", 5)
        self.whiskey = Drink("Old Fashioned", 12)
        self.drinks = [self.beer, self.whiskey]

    def test_customer_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_buy_a_drink(self):
        self.customer.buy_drink(self.beer)
        self.assertEqual(45, self.customer.wallet)