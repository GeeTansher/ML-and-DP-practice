import datetime
import speech_recognition as sr
import win32com.client as wc
import webbrowser
import openai
import os

speaker = wc.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio =  r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
        except Exception as e:
            return "Some Error occurred. Please speak again!"
        print(f"User said: {query}")
        return query
    
if __name__ == '__main__':
    say("hello i am Jarvis.")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://youtube.com"],
                 ["google","https://google.com"],
                 ["wikipedia","https://wikipedia.com"]]
        
        for site in sites:
            if f"open {site[0]}" in query.lower():
                webbrowser.open("site[1]")
                say(f"Opening {site[0]} sir...")
                
        if "open music" in query:
            music_path = ""
            os.system(f"open {music_path}")
            
        if "the time"   in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir time is {strfTime}")
        
        if "goodbye jarvis" in query.lower():
            say("Goodbye sir")
            break