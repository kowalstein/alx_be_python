""" This script demonstrates ann understanding of OOP by implementing
    a BankAccount class that encapsulates banking operations."""

class BankAccount:
    def __init__ (self, account_balance = 0):
        self.balance = account_balance

    def deposit(self, amount):
        amount = float (input ("How much do you want to deposit: "))
        self.balance += amount
    
    def withdraw(self, amount):
        amount = float (input ("How much do you want to withdraw: "))
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            return True
    
    def display_balance(self):
        return f"Current Balance: {self.balance}"
