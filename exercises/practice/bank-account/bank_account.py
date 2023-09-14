class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        if self.is_open:
            return self.balance
        else:
            raise ValueError("Account is closed.")

    def open(self):
        self.is_open = True

    def deposit(self, amount):
        if self.is_open:
            if amount < 0:
                raise ValueError("Amount must be positive.")
            self.balance += amount
        else:
            raise ValueError("Account is closed.")

    def withdraw(self, amount):
        if self.is_open:
            if amount < 0 or amount > self.balance:
                raise ValueError("Amount must be greater than 0.")
            self.balance -= amount
        else:
            raise ValueError("Account is closed.")

    def close(self):
        self.balance = 0
