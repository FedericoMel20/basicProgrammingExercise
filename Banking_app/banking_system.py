# banking_system.py

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        self.accounts[account_number] = Account(account_number, name)
        print(f"Account created for {name} with account number {account_number}.")

    def deposit_money(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist.")
        self.accounts[account_number].deposit(amount)

    def withdraw_money(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist.")
        self.accounts[account_number].withdraw(amount)

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist.")
        balance = self.accounts[account_number].get_balance()
        print(f"Balance for account {account_number} is {balance}.")
