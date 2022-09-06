

"""
Weather Program Python Project Using the requests library, create a program that will take a city name as input and return 
the current weather for that city.The program should also save the city name and the current weather to a file.
The program should also be able to read the file and print the city name and the current weather. 
Use this API to get the weather data: https://openweathermap.org/current
"""

import requests
import os
from dotenv import load_dotenv


def city_weather_checker():
    load_dotenv() 
    weather_url = os.getenv("WEATHER_DATA_URL")
    api_key = os.getenv("WEATHER_CHECKER_API_KEY")
    city = input("Enter a city name: ")
    city.lower()
    # check if city is valid
    if city == "":
        print("Invalid city name")
        return
    else :
        # get the weather data
        try:
            print("Getting weather data...")
            url = f"{weather_url}?q={city}&appid={api_key}"
            response = requests.get(url)
            # check if the response is valid
            if response.status_code == 200:
                # get the data
                data = response.json()
                # print(data)
                # get the weather and main data from the data dictionary 
                weather = data["weather"]
            
                # check if the file name doesnt exist, create it and write the data to it
                if not os.path.exists("weather.txt"):
                    with open("weather.txt", "w") as f:
                        f.write(f"{city} weather is : {weather[0]['main']}\nDescription: {weather[0]['description']}")
                        print("Weather data saved to file")
                # read the file and print the weather
                with open("weather.txt", "r") as file:
                    print("====== Weather status in {city} ======")
                    print(file.read())
            else:
                print("Invalid city name please try again")
                return
        except Exception as e:
            print(f"there was an error: {e}")
            return
        
def main():
    city_weather_checker()
    
if __name__ == "__main__":
    main()
            