import threading
from decimal import Decimal
class BankAccount:
    def __init__(self):
        self._balance = Decimal('0.00')
        self._lock = threading.Lock()
        self._is_open = False

    def get_balance(self):
        if not self._is_open:
            raise ValueError("account not open")
        return self._balance

    def open(self):
        if self._is_open:
            raise ValueError("Account is already open.")
        self._is_open = True

    def deposit(self, amount):
            raise ValueError("account not open")
            raise ValueError("Account is closed.")
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        with self._lock:
            self._balance += Decimal(amount)

    def withdraw(self, amount):
            raise ValueError("account not open")
            raise ValueError("Account is closed.")
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        with self._lock:
            if self._balance - Decimal(amount) < 0:
                raise ValueError("Insufficient funds.")
            self._balance -= Decimal(amount)

    def close(self):
        if not self._is_open:
            raise ValueError("account not open")
        self._is_open = False
