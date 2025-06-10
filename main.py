import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from google import genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "bef34fac283b4113b51f78b3e96c966a"

def speak(text):
    engine.say(text)
    engine.runAndWait() 

def aiprocess(command):
    client = genai.Client(api_key="AIzaSyCgZ6jhDcLNl8XQi8go2hUK2Z1vw4RinqA")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="You are a virtual assistant named Jarvis. You can open websites like Google, YouTube, Stack Overflow, GitHub, and Facebook. You can also play music and provide news updates. How can I assist you today?"
    )
    return response.text    

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open stack overflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():

        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])  # Get the list of articles

            # Print the headlines
            for i, article in enumerate(articles, start=1):
                speak(f"{i}. {article['title']}")
        else:
            # Integrating with open AI
            output = aiprocess(c)
            speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone 

        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)  
            word = r.recognize_google(audio)
            if  (word.lower() == "jarvis"):
                speak("Yes")
                # listen for word 
                with sr.Microphone() as source:
                    print("Jarvis Activated...")   
                    audio = r.listen(source)  
                    command = r.recognize_google(audio)

                    processCommand(command)


        except sr.UnknownValueError:
            print("Jarvis could not understand the audio") 
            speak("I could not understand what you said, please try again.")    
        except sr.RequestError as e:
            print("Jarvis error; {0}".format(e))