import requests
import json
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    i = 1
    speak("Today's headlines are:")
    a = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2021-11-09&sortBy=publishedAt&apiKey"
                     "=a75de97ef77146c28b7d85dc210678c9")
    news = a.text
    newsdict = json.loads(news)
    str = newsdict['articles']
    for s in str:
        speak(i)
        print(f"{i}. {s['title']}")
        speak(s['title'])
        i = i + 1
    speak("Thank you for listening!!!")
