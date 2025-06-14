from core.recognizer import listen
from core.tts import speak
from core.ai import generate_ai_response
from musicLibrary import music
from config import WAKE_WORD, NEWS_API_KEY
from utils.logger import setup_logger
from core.jokes import get_programmer_joke
from core.weather import get_weather
from core.wiki import search_wikipedia
from core.system_control import (
    open_notepad, open_calculator, open_chrome,
    shutdown_system, restart_system, lock_system
)

import requests
import webbrowser
import datetime
import os
import subprocess


log = setup_logger()

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return [article["title"] for article in articles]
    except Exception as e:
        log.error(f"Error fetching news: {e}")
        return []

def process_command(command: str):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif command.lower().startswith("play"):
        song = command.split(" ")[1]
        if song in music:
            webbrowser.open(music[song])
            speak(f"Playing {song}")
        else:
            speak("Song not found.")
    elif "news" in command.lower():
        headlines = fetch_news()
        if headlines:
            for i, h in enumerate(headlines[:5], start=1):
                speak(f"{i}: {h}")
        else:
            speak("No news right now.")
    elif "time" in command.lower():
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date"in command.lower():
        current_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today's date is {current_date}")
    elif "joke" in command.lower():
        joke = get_programmer_joke()
        speak(joke)
    elif "weather" in command.lower():
        weather_report = get_weather()
        speak(weather_report) 
    elif "who is" in command.lower() or "what is" in command.lower():
        query = command.lower().replace("who is", "").replace("what is", "").strip()
        if query:
            result = search_wikipedia(query)
            speak(result)
        else:
            speak("Please specify what you want to know about.")
    elif "open notepad" in command:
        open_notepad()

    elif "open calculator" in command:
        open_calculator()

    elif "open chrome" in command:
        open_chrome()

    elif "shutdown" in command:
        speak("Shutting down the system.")
        shutdown_system()

    elif "restart" in command:
        speak("Restarting the system.")
        restart_system()

    elif "lock the system" in command or "lock system" in command:
        speak("Locking the system.")
        lock_system()
    else:
        prompt = f"User said: {command}"
        response = generate_ai_response(prompt)
        speak(response)

def wait_for_wake_word():
    while True:
        heard = listen()
        if heard and WAKE_WORD in heard:
            speak("Yes?")
            return

def main():
    speak("Initializing Jarvis...")
    while True:
        wait_for_wake_word()
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
