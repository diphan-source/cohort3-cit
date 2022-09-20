
import sys 
import os
import secrets 
import hashlib 
import mysql.connector
import re
from time import sleep
from datetime import datetime

class Bank:
    def __init__(self , name , phone , pin ):
        self.name = name
        self.phone = phone
        self.pin = hashlib.sha256(pin.encode()).hexdigest()
        self.account_number = self.create_account_number()
        self.balance = 0
        self.logged_in = ""
        self.create_db()
        
        
        
    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "cit_bank"
            )
        except:
            raise mysql.connector.Error("Error Connecting to Database")
        
        c = conn.cursor()
        return conn , c
        
    def create_db(self):
        conn , c = self.connect_db()
        c.execute('''CREATE TABLE IF NOT EXISTS bank (id INT PRIMARY KEY AUTO_INCREMENT ,
                                name VARCHAR(255) , phone VARCHAR(10) NOT NULL ,
                                pin VARCHAR(255) NOT NULL ,
                                account_number VARCHAR(255) NOT NULL unique, 
                                balance INT )''')
        c.execute('''CREATE TABLE IF NOT EXISTS transactions (id INT PRIMARY KEY AUTO_INCREMENT ,
                                account_number VARCHAR(255) not null ,
                                amount INT not null,
                                date DATETIME default CURRENT_TIMESTAMP ,
                                transaction_type VARCHAR(255) NOT NULL)''')
        conn.commit()
        conn.close()
        print(f"Database Created Successfully")
             
    def create_account_number(self):
        # account number format 
        # AC + LAST 4 DIGITS OF PHONE + 6 RANDOM DIGITS
        # MAX 15 DIGITS
        account_number = 'AC' + \
            self.phone[-4:] + datetime.now().strftime("%Y%m%d") + \
                str(secrets.randbits(15))
        return account_number
    
    def create_account(self):
        conn , c = self.connect_db()
        sql = ('''INSERT INTO bank (name , phone , pin , account_number , balance)
               VALUES (%s , %s , %s , %s , %s)
               ''')
        data = (self.name , self.phone , self.pin , self.account_number , self.balance)
        
        try:
            c.execute(sql , data)
            conn.commit()
            conn.close()
            print("Account Created Successfully \n Your Account Number is : " + self.account_number)
        except mysql.connector.Error as err:
            print('Error : {}'.format(str(err)))
            conn.rollback()
        finally:
            c.close()
            conn.close()
            
    def get_balance(self):
        conn , c = self.connect_db()
        c.excetue('''SELECT balance FROM bank WHERE account_number = %s''', (self.logged_in))
        
        data = c.fetchone()
        conn.close()
        return data[0]
    
    def check_balance(self):
        print("Your Balance is : " + str(self.get_balance()))
        
    def update_database(self , transaction_type , amount):
        conn , c = self.connect_db()
        c.execute('''UPDATE bank SET balance = %s WHERE account_number = %s''', (self.balance , self.logged_in))
        sql = ('''INSERT INTO transactions (account_number , amount , transaction_type)
                VALUES (%s , %s , %s)''', (self.logged_in , amount , transaction_type))
        c.execute(sql)
        conn.commit()
        conn.close()
        print("database updated")
            
    def deposit(self,amount):
        self.balance = self.get_balance() + amount
        self.update_database("deposit" , amount)
        print("Deposit Successful")
        self.check_balance()
        
    def withdraw(self , amount):
        conn , c = self.connect_db()
        c.execute('''SELECT balance FROM bank WHERE account_number = %s''', (self.logged_in))
        if amount > self.get_balance():
            print("Insufficient Balance")
        else :
            self.balance = self.get_balance() - amount
            self.update_database("withdraw" , amount)
            print("Withdraw Successful")
            self.check_balance()
        conn.close()
        
    def transfer(self , account_number , amount):
        if amount <= self.get_balance():
            if self.transfer_to_account(account_number , amount):
                self.balance = self.get_balance() - amount
                self.update_database("transfer" , amount)
                print("Transfer Successful \n Your transfer {} to {}".format(amount , account_number))
                self.check_balance()
        else:
            print("Insufficient Balance")
            
    def transfer_to_account(self, account_number , amount):
        conn , c = self.connect_db()
        c. execute('''SELECT balance FROM bank WHERE account_number = %s''', (account_number,))
        data = c.fetchone()
        if data is None:
            print("Account Number not found")
            return False
        else:
            if data[0] == self.logged_in:
                print("You can't transfer to your own account")
                return False
            else:
                c.execute('''UPDATE bank SET balance = %s WHERE account_number = %s''', 
                          (data[0] + amount , account_number))
                conn.commit()
                conn.close()
                return True
            
    def login(self , account_number , pin):
        conn , c = self.connect_db()
        c.execute('''SELECT pin FROM bank WHERE account_number = %s''', (account_number))
        data = c.fetchone()
        conn.close()
        if data is None:
            print("Account Number not found")
            return False
        else:
            if data[3] == hashlib.sha256(pin.encode()).hexdigest():
                self.logged_in = account_number
                self.balance = data[5]
                print("Logged  Successfully")
                return True
            else:
                print("Incorrect Pin")
                return False
    def check_history(self):
        conn , c = self.connect_db()
        c.execute('''SELECT * FROM transactions WHERE account_number = %s''', (self.logged_in,))
        data = c.fetchall()
        c.close()
        conn.close()
        print("Transaction History:.......")
        for row in data:
            # Transfer of UGX: 5000 on Jan 19
            print(row[2] + ' of UGX: ' + str(row[3]) + ' on ' + str(row[4]))
            
    def exit(self):
        print("Thank You for Banking with us")
        sys.exit()
        
def clear_screen():
    sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
        
def check_phone(phone_number):
    return re.match(r'^(077|078|076|070|075)\d{7}$' , phone_number)
    
    

def main(Bank):
    print("Welcome to our Bank")
    print("1. Create Account \n 2. Login \n 3. Exit")
    user_input = input("Enter your choice : ")
        
    if user_input == "1":
        name = input("Enter your name : ")
        phone = input("Enter your phone number : ")
            
        while not check_phone(phone):
            print("Invalid Phone Number")
            phone = input("Enter your phone number : ")
                
        pin = input("Enter your pin : ")
        if not name or not phone or not pin:
            print("All fields are required")
            clear_screen()
            sys.exit()
        else:
            bank = Bank(name , phone , pin)
            bank.create_account()
    elif user_input == "2":
        account_number = input("Enter your account number : ")
        pin = input("Enter your pin : ")
        bank = Bank()
        if bank.login(account_number , pin):
            while True:
                print("1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Transfer \n 5. History \n 6. Exit")
                user_input = input("Enter your choice : ")
                if user_input == "1":
                    bank.check_balance()
                elif user_input == "2":
                    amount = int(input("Enter the amount you want to deposit: "))
                    bank.deposit(amount)
                    clear_screen()
                elif user_input == "3":
                    amount = int(input("Enter the amount you want to withdraw : "))
                    bank.withdraw(amount)
                    clear_screen()
                elif user_input == "4":
                    account_number = input("Enter the account number : ")
                    amount = int(input("Enter the amount you want to transfer: "))
                    bank.transfer(account_number , amount)
                    clear_screen()
                elif user_input == "5":
                    bank.check_history()
                    clear_screen()
                elif user_input == "6":
                    bank.exit()
                else:
                    print("Invalid Input")
        else:
            print("Login Failed :(")
            clear_screen()
    elif user_input == "3":
        sys.exit(-1)
    else: 
        print("invalid input")
        sys.exit(-1)
            
if __name__ == '__main__':
    main(Bank)