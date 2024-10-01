import os
import time
from pcinfo import Informtion_of_PC
from telegrambotmsg import Telegram_Bot_Sendtext
from shared import speak, take_command_over_voice
from intro import *
import webbrowser
import wikipedia
import pyautogui
import random
import subprocess
import urllib.request as ree




def connect(host='http://google.com'):
    try:
        ree.urlopen(host) 
        return True
    except:
        return False

def main():
    os.system('cls')
    # wishme()
    max_attempts = 2

    for i in range(max_attempts):
        if not connect():
            speak(f"Internet not connected. Attempt {i + 1} of {max_attempts}.")
            time.sleep(1)  
        else:
            speak("Internet connected.")
            break
    else:
        speak("Exceeded maximum attempts. Exiting program.")
        sys.exit()

    try:
        Telegram_Bot_Sendtext(Informtion_of_PC())
        import pywhatkit
    except:
        pass
    strTime = datetime.now().strftime("%I:%M")
    speak("The time is .....")
    speak(f"{strTime}")

    count = 0 
    
    while True:

        command = take_command_over_voice().lower()
        
        count += 1 

        if count % 5 == 0:
            os.system('cls')
            count = 0 

        


        if 'wikipedia' in command:
            try:
                speak("Searching on Wikipedia...")
                command = command.replace("search on wikipedia about", "").strip()
                results = wikipedia.summary(command, sentences=2)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("I couldn't find any Wikipedia page matching your request. Could you please try rephrasing?")
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for your query. Please be more specific.")
            except Exception as e:
                speak(f"An error occurred: {str(e)}")

        elif "time" in command:
            strTime = datetime.now().strftime("%I:%M:%S")
            speak(f"The time is {strTime}")

        elif "information" in command or "update" in command:
            message = Informtion_of_PC()
            Telegram_Bot_Sendtext(message) 


        elif "okay jarvis you are very good" in command or "you are very good" in command or  "you are good" in command or "very good" in command:
            speak ( " thank you sir ")
            speak("But i am just a assistant ")
        elif 'joke'in command or 'jokes' in command :
            import pyjokes
            speak("the joke is ")
            speak(pyjokes.get_joke())

        


        elif any(phrase in command for phrase in ["make a note", "write this down", "remember this"]):
            speak("What would you like me to write down?")
            note_text = take_command_over_voice()
            date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            file_name = f"{date}-note.txt"
            with open(file_name, "w") as f:
                f.write(note_text)
            
            # Attempt to open in Notepad (Windows)
            try:
                subprocess.Popen(["notepad.exe", file_name])
            except FileNotFoundError:
                speak("Sorry, I couldn't open Notepad. Please check the path.")
            
            speak("I've made a note of that")
        elif 'close this' in command:
            os.system("taskkill /f /im Notepad.exe")

        elif "remember that" in command:
            rememberMessage = command.replace("remember that", " ")
            rememberMessage = rememberMessage.replace("jarvis", "")
            speak("You told me that " + rememberMessage)
            remember = open("Remember.txt", "w")
            remember.write(rememberMessage)
            remember.close()

        elif "what do you remember" in command:
            remember = open("Remember.txt", "r")
            remember = remember.read()
            remember = remember.replace("remember that", " ")
            speak("You told me that" + remember)





        elif any(keyword in command for keyword in ['open in youtube', 'search on youtube']):
            search_query = command
            for keyword in ['open in youtube', 'search on youtube']:
                search_query = search_query.replace(keyword, '')
            search_query = search_query.strip()
            if search_query:
                url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}" 
                webbrowser.open(url)
                print(f"Opening YouTube search results for: {search_query}")
            else:
                print("No specific video query provided.")




        elif 'search ' in command:
            try:
                search_query = command.replace('search ', '').strip()
                pywhatkit.search(search_query)
                speak(f'Alright, opening search results for {search_query}')
            except Exception as e:
                speak(f"Sorry, I couldn't perform the search. Error: {str(e)}")

        elif "open youtube" in command :
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")   


        elif 'stack overflow' in command or 'stock overflow' in command:
            try:
                speak("Opening Stack Overflow")
                webbrowser.open("https://stackoverflow.com")
            except Exception as e:
                speak(f"Sorry, I couldn't open Stack Overflow. Error: {str(e)}")

 
        elif 'open chrome' in command :
            speak("opening chrome")
            webbrowser.open("https://www.google.co.in")
        




        elif 'play music' in command or 'play songs' in command or 'play song' in command:
            try:
                speak("Playing music")
                music_dir = 'E:\\songs'               
                if os.path.exists(music_dir):
                    songs = os.listdir(music_dir)                   
                    if songs:
                        rand = random.randint(0, len(songs) - 1)
                        os.startfile(os.path.join(music_dir, songs[rand]))
                    else:
                        speak("The music directory is empty. Please add some songs.")
                else:
                    speak("The specified music directory does not exist.")
            
            except Exception as e:
                speak(f"Sorry, I couldn't play music. Error: {str(e)}")

        elif 'stop music' in command or 'stop song' in command:
            pyautogui.press("f10")
            speak("Music paused")


        



        
        elif 'volume up' in command:
            pyautogui.press("volumeup")
        elif 'volume down' in command:
            pyautogui.press("volumedown")
        elif 'volume mute' in command or 'mute' in command:
            pyautogui.press("volumemute")
        elif 'set volume to 50' in command:
            pyautogui.press("volumemute")
            pyautogui.press("volumemute")            
            for _ in range(25):
                pyautogui.press("volumeup")           
            speak("Volume set to approximately 50 percent")


        
        elif "cancel shut down" in command or "cancel shutdown" in command  or "cancel" in command:
            sec = 1
            os.system( f'shutdown /a ')
            speak (f'Ok sir I am not shutting down your pc in next {sec} seconds')
        elif "shut down" in command or "shutdown" in command :
            sec = 300 
            os.system(f'shutdown /s /t {sec}') 
            speak (f'Ok sir I am shutting down your pc in next {sec} seconds')
        elif "restart" in command or "re start" in command or "rishta" in command  :
            sec = 300 
            os.system(f'shutdown /r /t {sec}')
            speak (f'Ok sir I am restarting your pc in next {sec} seconds')
        
        
        elif 'close chrome' in command :
            os.system("taskkill /f /im chrome.exe")
                
        
        
        elif "exit" in command :
            speak("jarvis will be closing ........Happy to help you ...... Thank you for using me sir  ")
            import sys
            sys.exit()
        
        else:
            speak("I'm not sure what you want me to do.")

if __name__ == "__main__":
    main()
