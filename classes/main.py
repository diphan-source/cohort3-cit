"""
Using classes, Create a basic banking application with the following features:

Create a class called BankAccount with the following attributes:

account_number - a string
balance - a float
owner - a string
type - a string
Create a class called Bank with the following attributes:

name - a string
accounts - a list of BankAccount objects
Create a class called Customer with the following attributes:

name - a string
accounts - a list of BankAccount objects
Create a class called Transactions with the following attributes:

 1. `account` - a `BankAccount` object
 2. `amount` - a float
 3. `type` - a string
The application should have the following functionality:

Create a new Bank object
Create a new Customer object
Create a new BankAccount object
Add the BankAccount object to the Bank object
Add the BankAccount object to the Customer object
Print the Bank object
Print the Customer object
Print the BankAccount object
Create a new Transaction object
Add the Transaction object to the BankAccount object

"""

import random
import uuid
import datetime


class Bank:
    def __init__(self, name:str):
        self.name = name
        self.accounts = []
        
        
    def add_account(self, account):
        self.accounts.append(account)
        
        
    def __str__(self):
        return f"Welcome to {self.name} Bank. We have {len(self.accounts)} accounts"

class BankAccount(Bank):
    def __init__(self, name , balance=0.0):
        super.__init__(self, name)
        self.account_number = self.create_account_number()
        self.balance = balance
        self.owner = self.create_owner()
        self.type = self.account_type()
    
    
    def create_owner(self):
        owner  = input("Enter your name: ")
        return owner
   
    def create_account_number(self):
        return str(uuid.uuid4())[:8].lower()
   
    def account_type(self):
        type = input("Enter Account Type: ")
        return type
    
        
    def __str__(self):
        return f" Hello {self.owner} your Account Number is {self.account_number} \
            which is a {self.type} and your outstanding Balance is {self.balance}"
    
            
class Customer(BankAccount):
    def __init__(self, name, owner, type, balance):
        super.__init__(self, name, owner, type, balance)
        self.accounts = []
        
    def __str__(self):
        return super().__str__()
    
class Transactions(BankAccount):
    def __init__(self ,name ,balance ,  amount:float , type:str):
        super.__init__(self,name , balance)
        self.amount = amount
        self.type = type
        self.withdraw = self.withdraw()
        self.deposit = self.deposit()
        
    def withdraw(self):
        if self.amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= self.amount
            return self.balance
        
    def deposit(self):
        if self.amount < 0:
            print("Invalid Amount")
        else:
            self.balance += self.amount
            return self.balance
        
    def __str__(self):
        return f"Your new balance is {self.balance}\
            and your transaction type is {self.type} at  {datetime.datetime.now()}"
    
def Create_Bank():
    bank= input("Enter Bank Name: ")
    print(f"Welcome to {bank} Bank")
    return Bank(bank)

def Create_Customer():
    name = input("Enter Customer Name: ")
    print(f"{name} Welcome to our Bank")
    return f"Hello {name} your Account Number is "

def main():
   bank = Create_Bank()
   while True:
       print("1. Create Account")
       print("2. Deposit")
       print("3. Withdraw")
       print("4. Exit")
       choice = int(input("Enter Choice: "))
       if choice == 1:
           customer = Create_Customer()
           account_type = input("Enter Account Type: ")
           account = BankAccount(bank.name, customer.name, account_type)
           bank.add_account(account)
           customer.accounts.append(account)
       elif choice == 2:
           account_number = input("Enter Account Number: ")
           for account in bank.accounts:
               if account.account_number == account_number:
                   amount = float(input("Enter Amount: "))
                   account.deposit(amount)
                   print(account)
                   break
       elif choice == 3:
           account_number = input("Enter Account Number: ")
           for account in bank.accounts:
               if account.account_number == account_number:
                   amount = float(input("Enter Amount: "))
                   account.withdraw(amount)
                   print(account)
                   break
       elif choice == 4:
           break
       else:
           print("Invalid Choice")
           
if __name__ == "__main__":
    main()
        