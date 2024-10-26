from .bank_account import BankAccount

# account/checking_account.py
from .bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_number: str, balance: float = 0.0):
        super().__init__(account_number, balance)
        self._transactions = []  # Private attribute to store transactions

    def deposit(self, amount: float):
        """Override the deposit method to include transaction logging."""
        self._deposit(amount)
        self.log_transaction(f"Deposited {amount}")

    def withdraw(self, amount: float):
        """Override the withdraw method to include transaction logging."""
        self._withdraw(amount)
        self.log_transaction(f"Withdrew {amount}")

    def log_transaction(self, transaction: str):
        """Overrides the base log_transaction method to log each transaction."""
        # Add transaction to the list
        self._transactions.append(transaction)
        # Here, you can add more specific logging behavior if needed
        print(f"CheckingAccount transaction logged: {transaction}")

    def get_transactions(self):
        """Returns the list of all transactions."""
        return self._transactions
