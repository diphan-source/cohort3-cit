""" 
Password Generator Python Project
Create a program that generates a random password for the user. 
Ask the user how long they want their password to be, and how many letters and numbers they want in their password. 
Have a mix of upper and lowercase letters, as well as numbers and symbols. 
The password should be a minimum of 6 characters long.

"""


import random
import string


def random_password_gen():
    print("Welcome to the Password Generator!")
    # how long do you want your password to be?
    length = int(input("How long do you want your password to be? "))
    # how many letters do you want in your password?
    letters = int(input("How many letters do you want in your password? "))
    # how many numbers do you want in your password?
    numbers = int(input("How many numbers do you want in your password? "))
    # how many symbols do you want in your password?
    symbols = int(input("How many symbols do you want in your password? "))
    # create a list of letters, numbers, and symbols
    password = ""
    
    # minimum of 6 characters
    if length < 6:
        print("\nYour password must be at least 6 characters long.")
        return random_password_gen()
    else:
        for i in range(letters):
            password += random.choice(string.ascii_letters)
        for i in range(numbers):
            password += random.choice(string.digits)
        for i in range(symbols):
            password += random.choice(string.punctuation)
        password = list(password)
        random.shuffle(password)
        password = "".join(password)
        return password
    

print(f"Your password is: {random_password_gen()}")
    
        
            
    
    
    