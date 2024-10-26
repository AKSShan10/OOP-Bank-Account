from .bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        """Public method to access the private deposit method in the base class."""
        self._deposit(amount)

    def withdraw(self, amount: float):
        """Public method to access the private withdraw method in the base class."""
        self._withdraw(amount)

    def calculate_interest(self):
        """Calculates and returns the interest based on the current balance and interest rate."""
        interest = self.get_balance() * self.interest_rate
        print(f"Interest calculated: {interest}")
        return interest