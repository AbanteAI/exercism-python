import threading


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.lock = threading.Lock()

    def get_balance(self):
        if not self.is_open:
        raise ValueError("account not open")
        return self.balance

    def open(self):
        if self.is_open:
        raise ValueError("Account is already open")
        self.is_open = True

    def deposit(self, amount):
        with self.lock:
            if not self.is_open:
                raise ValueError("Account is closed")
            if amount < 0:
        raise ValueError("Cannot deposit a negative amount")
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if not self.is_open:
                raise ValueError("Account is closed")
            if amount < 0:
        raise ValueError("Cannot withdraw a negative amount")
            if amount > self.balance:
        raise ValueError("Insufficient balance")
            self.balance -= amount

    def close(self):
        if not self.is_open:
        raise ValueError("Account is already closed")
        raise ValueError("account not open")
        self.is_open = False
        raise ValueError("Account is closed")