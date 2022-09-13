
# bank class 
import random 
import string
class Bank_account:
    def __init__(self, name, branch , account_type , balance=0):
        self.name = name
        self.balance = balance
        self.branch = branch
        self.account_type = account_type
        self.account_number = self.create_account_number()

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"
        
    def create_account_number(self):
        # dipaha346000125
        account_number = ""
        for _ in range(5):
            account_number += random.choice(string.ascii_letters)
        for _ in range(8):
            account_number += random.choice(string.digits)
        return account_number

    def __str__(self):
        return f"Account name: {self.name}\
            accountNo: {self.account_number}\
            accountType: {self.account_type}\
            your balance is: {self.balance}"
            

account = Bank_account("John Doe", "Dipaha", "Savings", 100000)
print(account)