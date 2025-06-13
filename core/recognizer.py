import speech_recognition as sr
import logging
from core.tts import speak

log = logging.getLogger(__name__)

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
        except sr.WaitTimeoutError:
            log.warning("Timeout: No speech detected.")
            speak("I didn't hear anything, please try again.")
    return None
