import speech_recognition as sr
import logging
import webbrowser
import pyttsx3
import musicLibrary
import requests
from google import genai

# constants:
WAKE_WORD = "jarvis"
newsapi = "bef34fac283b4113b51f78b3e96c966a"
GENAI_API_KEY = "AIzaSyCgZ6jhDcLNl8go2hUK2Z1vw4RinqA"


# logger setup:
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


engine = pyttsx3.init()          #TTS engine


def speak(text: str):
    engine.say(text)
    engine.runAndWait() 
  

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        log.info("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            log.info(f"Recognized: {command}")
            return command.lower()
        except sr.UnknownValueError:
            log.warning("Could not understand the audio.")
            speak("I could not understand what you said, please try again.")
        except sr.RequestError as e:
            log.error(f"Error with the speech recognition service: {e}")
            speak("There was an error with the speech recognition service, please try again later.")
    return None

def fetch_news():
    # Fetch top news headlines using NewsAPI
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        articles = response.json().get("articles", [])
        return [article["title"] for article in articles]
    except Exception as e:
        log.error(f"Error fetching news: {e}")
        return []

def generate_ai_response(prompt: str):  
    # Generate a response from Gemini AI model.
    try:
        client = genai.Client(api_key=GENAI_API_KEY)
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents = prompt
        )
        return response.text
    except Exception as e:
        log.error(f"Gemini AI error: {e}")
        return "I encountered an error while trying to process your request with AI."


def process_command(command: str):
    # Process the user’s command and take action.
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open stack overflow" in command.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in command.lower():
        webbrowser.open("https://github.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak(f"playing {song}")
        if link not in song:
            speak("Song not found in the library.")
    elif "news" in command.lower():
        headlines = fetch_news()
        if headlines:
            for i, headlines in enumerate(headlines[:5], start=1):
                speak(f"{i}: {headlines}")
            else:
                speak("No news articles found.")
    else:
        prompt = f"You are a virtual assistant named Jarvis. User said: {command}"
        output = generate_ai_response(prompt)
        speak(output)

def wait_for_wake_word():
    # Wait until the wake word is detected.
    while True:
        heard = listen()
        if heard and WAKE_WORD in heard.lower():
            speak("Yes?")
            return

def main():
    speak("Intializing Jarvis...")
    while True:
        wait_for_wake_word()
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()