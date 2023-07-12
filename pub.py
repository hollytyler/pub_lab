class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def change_till_by_amount(self, amount):
        self.till += amount
                
    def sell_drink(self, drink, customer):
        customer.buy_drink(drink)
        self.change_till_by_amount(drink.price)

