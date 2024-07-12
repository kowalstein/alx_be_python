""" This script demonstrates ann understanding of OOP by implementing
    a BankAccount class that encapsulates banking operations."""

class BankAccount:
    def __init__ (self, account_balance = 0):
        self.balance = account_balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            return False
        else:
            self.balance = self.balance - amount
            return True, self.balance
    
    def display_balance(self):
        print (f"Current Balance: ${self.balance:.2f}")
        return
