import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as kit
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init('sapi5') #sapi windows provide in built voice so use for taking voice as input
voices = engine.getProperty('voices')

# print(voices[1].id)


url='https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')

# to set voice
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning')

    elif hour>12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    
    speak("I am Eidith sir , Please tell me how may I help you")        


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # if i am speaking after 1 sec then my model should wait it should not terminate the program
        r.pause_threshold = 1
        audio = r.listen(source)
        

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            # print(e)    
            print("Say that again please...")   #Say that again will be printed in case of improper voice 
            return "None" #None string will be returned
        return query


if __name__ == "__main__":
    # speak("Kaushik is good boy")
    wishme()

    while True:
        query = takeCommand().lower()
        # Logic for Executing tasks based on query  

        if 'wikipedia' in query:
            speak('Searching Wekipedia......')
            query=query.replace("wekipedia","") #here it will replcae wikipedia
            results = wikipedia.summary(query,sentences=2) # here sentences=2 means will read 2 sentences from wikipedia
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play' in query:
            music = query[5:]
            kit.playonyt(query)

        elif "headlines" in query:
                
                unwanted = ['BBC World News TV', 'BBC World Service Radio','News daily newsletter', 'Mobile app', 'Get in touch']

                for x in list(dict.fromkeys(headlines)):
                    if x.text.strip() not in unwanted:
                        headlines = x.text.strip()        
                        engine.say(headlines+" ")
                        engine.runAndWait() 
                       

        elif 'shutdown' in query:
            break 

        elif 'the time' in query:
            timeStr = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is :{timeStr}")

        elif 'open vs code' in query:
            path = "E:\Microsoft VS Code\Code.exe"
            os.startfile(path)
              

        elif 'open file explore' in query:
            openfe = 'C:\\Home'
            os.startfile(openfe)

        elif 'open e drive' in query:
            directory = 'E:\\'
            os.startfile(directory) 
            os.walk(directory)
            