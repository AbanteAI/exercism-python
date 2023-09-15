class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        raise ValueError("account not open")
            raise ValueError("Account is closed")
        return self.balance

    def open(self):
        if self.is_open:
        raise ValueError("Account is already open")
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
        raise ValueError("account not open")
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
        raise ValueError("account not open")
        if amount < 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def close(self):
        self.is_open = False
        self.balance = 0