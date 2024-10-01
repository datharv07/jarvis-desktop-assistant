from shared import speak
from datetime import *

def wishme ():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    # speak("Caliberating and examining all the core processors")
    # speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.now().hour)
    if hour == 5 and hour <= 12 :
        speak("Good Morning Atharv")
    else:
        speak("Good Afternoon Atharv")
  
    speak('''Hello sir, i am JARVIS , your desktop assistant.....
    how may i help you''')