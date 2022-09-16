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
import sys


class BankAccount():
    def __init__(self, balance=0.0):
        self.account_number = self.generate_account_number()
        self.balance = balance
        self.owner = self.create_owner()
        self.type = self.account_type()
    
    
    def create_owner(self):
        owner  = input("Enter your Fullname: ")
        return owner
   
    def generate_account_number(self):
        account_num = 'AC' + \
            str(random.randint(1000000000, 9999999999)) + \
            str(uuid.uuid4())[:4].lower()
        return account_num
   
    def account_type(self):
        Account_types = ["Savings", "Current" , "Fixed Deposit" , "Recurring Deposit"]
        print("Choose your Account Type")
        print("1. savings\n2. current\n3. fixed Deposit\n4. recurring Deposit")
        type = input("Enter Account Type: ")
        for i in range(len(Account_types)):
            if type == str(i+1):
                return Account_types[i]
            else:
                return "Invalid Account Type"
    def __repr__(self):
        return f"Bank Name: {self.owner} \n Account_num: {self.account_number}\n Account_type: {self.type}"
            
    

class Bank():
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        return self.accounts.append(account)
    
    def __str__(self):
        return f"Bank Name: {self.name} \n Accounts: {self.accounts}"
            
class Customer(Bank):
    def __init__(self , name):
       super().__init__(name)
       
    def __str__(self):
        return f"Customer Name: {self.name} \n Accounts: {self.accounts}"
    
class Transactions(BankAccount):
    def __init__(self ,account_number ,owner ,balance ,  amount:float , type:str):
        super().__init__(owner, type, balance , account_number)
        self.amount = amount
        self.withdraw = self.withdraw()
        self.deposit = self.deposit()
        
    def withdraw(self):
        if self.amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= self.amount
            return f"Your account has been debited with {self.amount}\
                at {datetime.datetime.now()}"
        
    def deposit(self):
        if self.amount < 0:
            print("Invalid Amount")
        else:
            self.balance += self.amount
            return f"Your account has been credited with {self.amount}\
                at {datetime.datetime.now()}"
                
    def transaction(self):
        return f"Your new balance is {self.balance}\
            and your transaction type is {self.type} at  {datetime.datetime.now()}"
        
    
    
def Create_Bank():
    bank= input("Enter Bank Name: ")
    return (Bank(bank))

def Create_Customer():
    return (Customer(input("Enter Customer Name: ")))
    
    
def create_bank_account():
    account = BankAccount()
    print(account)
    return account

# create a function to add the bank account object to the bank object
def add_account_to_bank(bank, account):
    bank.add_account(account)
    
def add_account_to_customer(customer, account):
    customer.add_account(account)
    
def create_transaction(BankAccount):
    amount = float(input("Enter Amount: "))
    type = input("Enter Transaction Type: ")
    transaction = Transactions(BankAccount.account_number, BankAccount.owner, BankAccount.balance, amount, type)
    BankAccount.balance = transaction.balance
    print(transaction.transaction())
    return transaction

def add_transaction_to_bankaccount(account, transaction):
    account.add_transaction(transaction)
    

def main():
    print("Welcome to Basic Banking Application")
    print("1. Create a new bank \n2. Create a new Customer\n3. Create a new Bank Account\n4. Create a new Transaction\n5. Exit")
    choice = input("Enter your option: ")
    if choice == "1":
        bank =Create_Bank()
        print(bank)
    elif choice == "2":
        customer = Create_Customer()
        print(customer)
    elif choice == "3":
         create_bank_account()
    elif choice == "4":
        transaction = create_transaction(BankAccount)
        print(transaction)
    elif choice == "5":
        print("Thank you for using Basic Banking Application")
        sys.exit()
    else:
        print("Invalid Option")
        
if __name__ == "__main__":
    main()
        