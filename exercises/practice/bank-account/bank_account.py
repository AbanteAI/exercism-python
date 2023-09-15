class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        if self.is_open:
            return self.balance
        raise ValueError("Account is closed.")

    def open(self):
        if not self.is_open:
            self.is_open = True
            self.balance = 0

    def deposit(self, amount):
        if self.is_open and amount >= 0:
            self.balance += amount
        else:
            raise ValueError("Invalid deposit amount or account is closed.")

    def withdraw(self, amount):
        if self.is_open and amount >= 0 and self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Amount must be greater than 0, insufficient balance, or account is closed.")

    def close(self):
        if self.is_open:
            self.is_open = False
            self.is_open = False
