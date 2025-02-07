''' Write a Python class BankAccount with attributes like account_number, balance, 
date_of_opening and customer_name, and methods like deposit, withdraw, and check_balance.'''
class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
        
account = BankAccount("123456789", "John Doe", 5000, "2022-01-15")
account.check_balance()
account.deposit(1500)
account.withdraw(2000)
account.check_balance()
