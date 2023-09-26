class User:
    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0.0

    def add_debt(self, user, amount):
        self.owes[user.name] = amount
        user.owed_by[self.name] = amount

    def add_payment(self, user, amount):
        self.owed_by[user.name] -= amount
        user.owes[self.name] -= amount

    def update_balance(self):
        self.balance = sum(self.owed_by.values()) - sum(self.owes.values())