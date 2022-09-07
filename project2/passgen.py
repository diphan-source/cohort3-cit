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
    letter_no = int(input("How many letters do you want in your password? "))
    # how many numbers do you want in your password?
    number_no = int(input("How many numbers do you want in your password? "))
    
    letters = string.ascii_letters
    num = string.digits
    symbols = string.punctuation
    
    # generate a random password containing letters, numbers and symbols
    random_pass = f"{letters}{num}{symbols}"
    # convert the random password into a list and shuffle it
    password = list(random_pass)
    random.shuffle(password)
    
    # generate random password and convert to string
    random_password = random.choices(password  , k = length)
    random_password = "".join(random_password)
    # print("Your random password is:", random_password) for testing purposes
    # check if the password contains letter_no , number_no and minimum length of 6
    if len(random_password) >=6 :
        # check if there are letter_no letters in the password
        if sum(c.isalpha() for c in random_password) == letter_no:
            # check if there are number_no numbers in the password
            if sum(c.isdigit() for c in random_password) == number_no:
                print("Your random password is:", random_password)
            else:
                print("Your password does not contain the specified numbers .")
        else:
            print("Your password does not contain the specified letters.")
    else:
        print("Your password should be at least 6 characters long.")
    return f"your password is: {random_password}"
        
random_password_gen()
            
    
    
    