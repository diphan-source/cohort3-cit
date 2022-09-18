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


# dictionary to store BankAccount objects
store_data = {}
class BankAccount():
    def __init__(self, balance=0.0 ):
        self.account_number = self.generate_account_number()
        self.balance = balance
        self.owner = self.create_owner()
        self.type = self.account_type()
    
    def create_owner(self):
        print("welcome to our Bank")
        owner  = input("Enter your Fullname: ")
        return owner
    
    @staticmethod
    def generate_account_number():
        account_num = 'AC' + \
            str(random.randint(1000000000, 9999999999)) + \
            str(uuid.uuid4())[:4].lower()
        return account_num
   
    @staticmethod
    def account_type():
        print("Choose your Account Type")
        print("1. savings\n2. current\n3. fixed Deposit\n4. recurring Deposit")
        type = input("Enter Account Type: ")
        if type == '1':
            return 'savings'
        elif type == '2':
            return 'current'
        elif type == '3':
            return 'fixed Deposit'
        elif type == '4':
            return 'recurring Deposit'
        else :
            print("Invalid Account Type")
            sys.exit()    
    
    
    def __repr__(self):
        return f"\n Account_Name: {self.owner} \n Account_no: {self.account_number} \
            \n Account_type: {self.type}\
            \n has been created at {datetime.datetime.now()}"
            
    def add_to_store(self):
        store_data[self.account_number] = self
        return store_data
            
    

class Bank():
    def __init__(self):
        self.name = self.create_bank()
        self.accounts = self.types_bank_accounts()

    def create_bank(self):
        self.name = input("Enter Bank Name: ")
        return f"Welcome to {self.name} Bank"
    
    def types_bank_accounts(self):
        # display the types of accounts
        available_acc = ['savings', 'current', 'fixed Deposit', 'recurring Deposit']
        return available_acc
        
        
    def __str__(self):
        return f"{self.name} \n Accounts_available :{self.accounts}"
            
class Customer():
    def __init__(self):
        self.name = self.create_customer()
        # self.accounts = self.add_accounts(BankAccount())
       
    def create_customer(self):
        self.name = input("Enter your Fullname: ")
        self.account_number=BankAccount.generate_account_number()
        self.type=BankAccount.account_type()
        return f"Welcome {self.name} your account has been created"
          
    def __repr__(self) :
        return f"{self.name} \n AccountNo: {self.account_number} \n AccountType:{self.type} \n created at {datetime.datetime.now()}"
    
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
                
    def add_transaction_to_account(self, account):
        account.transactions.append(self)
                
    def transaction(self):
        return f"Your new balance is {self.balance}\
            and your transaction type is {self.type} at  {datetime.datetime.now()}"
        
        
def main():
    while True:
        print("Welcome to our Bank")
        print("1. Create Bank\n2. Create Customer\n3. Create BankAccount\n4. Create Transaction\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            bank = Bank()
            print(bank)
        elif choice == '2':
            customer = Customer()
            print(customer)
        elif choice == '3':
            account = BankAccount()
            print(account)
        elif choice == '4':
            transaction = Transactions()
            print(transaction)
        elif choice == '5':
            sys.exit()
        else:
            print("Invalid Choice")
            sys.exit()
        
if __name__ == "__main__":
    main()
    
    

