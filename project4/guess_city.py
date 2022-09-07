

import requests
import random
import json
from dotenv import load_dotenv
import os
# get the url from the .env file
load_dotenv()
url = os.getenv('COUNTRY_CITY_URL')

def country_city_guess_game():
    # get the list of countries and their capitals
    fetch_data = requests.get(url)
    data = fetch_data.json()
    correct_ans = 0
    incorrect_ans = 0
    for i in range(10):
        random_country = random.choice(data)
        print("What is the capital of", random_country["country"], "?")
        user_answer = input("Enter your answer: ")
        if user_answer == random_country["city"]:
            print("Correct!")
            correct_ans += 1
        else:
            print("Incorrect!")
            incorrect_ans += 1
    print("You got", correct_ans, "correct answers and", incorrect_ans, "incorrect answers.")

def main():
    country_city_guess_game()
    
if __name__ == "__main__":
    main()