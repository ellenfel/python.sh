from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Kansas City"):
    requests_url= f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={os.getenv("API_KEY")}&q={city}'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n***Get weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)