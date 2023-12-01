import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from googletrans import Translator
import wikipedia as googlescrap
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import keyboard
import sys
from keyboard  import press_and_release
from pyautogui import click
from keyboard import write
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',173)



def speak(audio): 
    print(" ")
    engine.say(audio)
    print(f": {audio}")
    print(" ")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning,sir!")
        

    elif hour>=12 and hour<18:
        speak("Good Afternoon,sir ")
        

    else:
        speak("Good Evening,sir!")

    speak("how may i help you ,sir")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said: {query}") 
    
    except Exception as e:
        print("say that again please....")
        return "None"
    return query


def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
         print("Recognizing...")
         query = r.recognize_google(audio,language='hi')
         print(f"you said: {query}") 
    
        except Exception as e:
         print("say that again please....")
         return "None"
        return query      

def Temp():
    search = "https://www.google.com/search?q=today+temperature&oq=today+tem&aqs=chrome."
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").Text
    speak(f"The Temperature is{temperature} celcius")

def Tran():
    speak("Tell Me the line!")
    line = TakeHindi()
    traslate = Translator()
    result = traslate.translate(line)
    Text = result.text
    speak("The Translation for This Line Is:"+Text)


if __name__ == "__main__":
    

    wishMe()

    while True:
      query = takecommand().lower()

 # logic for excuting task based on query

      if 'wikipedia' in query:
         speak("Searching wikipedia")
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=3)
         speak("According to wikipedia")
         print(results)
         speak(results)
        
      elif'hello jarvis'in query:
          speak("hello,sir")

      elif 'open powerpoint' in query:
           webbrowser.open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
           speak("wait a second")


      elif 'open google' in query:
               webbrowser.open("google.com")
               speak("opening,google,wait a second")

      elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir the time is{strTime}")

      elif 'open wordpad' in query:
         os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
         speak("ok,sir wait a second")

      elif 'take a break' in query:
             speak("ok")
             speak("have a good day ,sir ") 
             break 

      elif 'who are you' in query:
          speak("i am your persional assistant,jarves sir")

      elif 'tell me about yourself' in query:
          speak("My name is jarves and i am your persional assistant,sir")
           
      elif 'how old are you' in query:
          speak("I was launched in 2020,but i am wise beyond my years")
             
      elif 'good night ,jarvis' in query:
          speak("Good night ,sir,sweet dream")
        
      elif 'good morning ,jarvis'in query:
          speak("Good morning ,sir")

      elif 'do not ask me ' in query:
             
          speak("sorry,sir")

      elif 'good job ,jarvis'in query:
          speak("Thank you ,sir")

      elif 'good job' in query:
          speak("Thank you,sir")

      elif 'who are you jarvis' in query:
          speak("you are asking me who am i by taking my name,sir")

      elif'what is your name' in query:
          speak(" jarves and also you can call me lucifer,god of hell")
 
      
    #   elif 'downloading speed' in query:
    #       SpeedTest()

    #   elif 'uploading speed' in query:
    #        SpeedTest()

    #   elif 'internet speed' in query:
    #       SpeedTest()

      elif 'transform' in query:
          Tran()

      elif'search' in query:
         import pywhatkit
         query = query.replace("jarves","")
         query = query.replace("google search","")
         query = query.replace("google","")
         speak("this is what i found on the web!")
         pywhatkit.search(query)

         try:
              result = googlescrap.summary(query,2)
              speak(result)

         except:
              speak("no found data")

      elif'temperature' in query:
          Temp()
          

      elif'how to' in query:
          speak("wait a second")
          op = query.replace("jarves","")
          max_result = 1
          how_to_func = search_wikihow(op,max_result)
          assert len(how_to_func)==1
          how_to_func[0].print()
          speak(how_to_func[0].summary)

      elif'open facebook'in query:
          webbrowser.open('https://www.facebook.com/')
          speak("ok,sir,wait a second")


      elif'open youtube'in query:
          webbrowser.open('https://www.youtube.com/')
          speak("ok ,sir")
    
        
      elif'tell me a joke' in query:
          speak("two friends visit a stadium!first,why are all these people running?,second,this is a race,the winner wiil get the cup!first,if only winner will get the  cup,then why are other running")
          
      elif'open vs' in query:
           os.startfile("C:\\Users\\Aman Jain\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
           speak("wait a second")
      

      elif'open chrome' in query:
          os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
          speak("ok,sir")

      elif'close vs code'in query:
          os.system("TasKill /F /in Code.exe")
          speak("ok,sir")

      elif'close chrome'in query:
          os.system("TasKill /F /in chrome.exe")
          speak("As u wish")

    
         
      elif'open excel'in query:
          os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
          speak("ok,sir")

      elif'you can sleep now'in query:
          speak("ok,sir")
          sys.exit() 

      elif'stop'in query:
          keyboard.press('space bar')
          speak("done,sir")

      elif'skip' in query:
          keyboard.press('l')

      elif'mute'in query:
          keyboard.press('m')
          speak("ok,sir")

      elif'full screen'in query:
          keyboard.press('f')
          speak("don,sir")
        
      elif'new tab'in query:
            press_and_release('ctrl + t')

      elif'close tab'in query:
            press_and_release('ctrl + w')
        
      elif'new window'in query:
            press_and_release('ctrl + n ')

      elif'minimise all' in query:
          press_and_release("ctrl + A ")


    








