import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
# import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "bef34fac283b4113b51f78b3e96c966a"

def speak(text):
    engine.say(text)
    engine.runAndWait() 

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
    # elif "news" in c.lower():
    #     r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")

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