from .bank_account import BankAccount

class Customer:
    def __init__(self, name: str, customer_id: str):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account: BankAccount):
        self.accounts.append(account)
        print(f"Account {account.account_number} added for customer {self.name}.")
