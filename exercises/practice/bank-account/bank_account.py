from threading import Lock

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.balance = 0
        self.is_open = False
        self.is_open = False
        self.lock = Lock()
        self.lock = Lock()

    def get_balance(self):
        if not self.is_open:
            raise ValueError("Account is closed")
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError("Account is already closed")
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError("Account is closed")
        if amount < 0:
            raise ValueError("Invalid deposit amount")
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError("Account is closed")
        if amount < 0:
            raise ValueError("Invalid withdrawal amount")
        with self.lock:
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            self.balance -= amount

    def close(self):
        if not self.is_open:
            raise ValueError("Account is already closed")
        self.is_open = False
        self.balance = 0