import requests
from config import WEATHER_API_KEY
import logging

log = logging.getLogger(__name__) 

def get_weather(city="mumbai"):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        report = f"The current temperature in {city} is {temp}°C with {weather_desc}. Humidity is {humidity}%, and wind speed is {wind} m/s."
        return report
    
    except Exception as e:
        log.error(f"Error fetching weather data: {e}")
        return "I couldn't fetch the weather information right now. Please try again later."