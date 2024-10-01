# shared.py
import pyttsx3
import speech_recognition as sr
from datetime import *

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 9999)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command_over_voice():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Automatically adjust energy threshold
        audio = r.listen(source,timeout=10,phrase_time_limit=20)
        print (10/0)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in').lower()
        print(f'You said: {command}')
        return command
    except Exception as e:
        print("Please try again")
        return take_command_over_voice()  # Retry on error
    


