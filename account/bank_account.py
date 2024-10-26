class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        self.account_number = account_number
        self.__balance = balance  # Private attribute with stricter encapsulation

    def _deposit(self, amount: float):
        """Private method for depositing money."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def _withdraw(self, amount: float):
        """Private method for withdrawing money."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def log_transaction(self, transaction: str):
        """Logs the transaction details (base method)."""
        print(f"Transaction logged: {transaction}")