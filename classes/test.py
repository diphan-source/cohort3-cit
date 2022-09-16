"""
Create a class called BankAccount with the following attributes:

account_number - a string
balance - a float
owner - a string
type - a string
Create a class called Bank with the following attributes:

name - a string
accounts - a list of BankAccount objects
Create a class called Customer with the following attributes:

"""

class BankAccount():
    def __init__(self, owner, type, balance, account_number):
        self.owner = owner
        self.type = type
        self.balance = balance
        self.account_number = account_number
        
    def __str__(self):
        return f" Hello {self.owner} your Account Number is {self.account_number} \
            which is a {self.type}'s and your outstanding Balance is {self.balance}"
            
class Bank():
    def __init__(self, name):
        self.name = name
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
        
    def __str__(self):
        return f"Welcome to {self.name} Bank, we have {len(self.accounts)} accounts"
    
"""
Create a class called Transactions with the following attributes:

 1. `account` - a `BankAccount` object
 2. `amount` - a float
 3. `type` - a string
"""
class Transactions():
    def __init__(self, account, amount, type):
        self.account = account
        self.amount = amount
        self.type = type