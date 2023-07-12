class Customer:
    def __init__(self, name, wallet, age, drunkness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_drink(self, drink):
        self.reduce_wallet(drink.price)

    def drunkness_level_increase(self, drunkness):
        if self.customer

