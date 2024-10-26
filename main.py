# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# main.py
from account.customer import Customer
from account.savings_account import SavingsAccount
from account.checking_account import CheckingAccount

def main():
    # Create a customer
    customer = Customer(name="John Doe", customer_id="C001")

    # # Create a savings account and checking account
    savings = SavingsAccount(account_number="SA001", balance=1000)
    checking = CheckingAccount(account_number="CA001", balance=500)
    #
    # Add accounts to the customer
    customer.add_account(savings)
    customer.add_account(checking)
    #
    # Perform transactions
    savings.deposit(200)
    savings.calculate_interest()

    checking.deposit(100)
    checking.withdraw(50)

if __name__ == "__main__":
    main()

