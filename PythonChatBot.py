import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import time
MASTER = 'Sir'
print("Initializing F.A.M.I")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)
newVoiceRate = 140
#voice.name == 'Alex'

engine.setProperty('rate',newVoiceRate)
#speak function will speak whatever string will pass through it
def speak(text):
    engine.say(text)
    engine.runAndWait()
speak('Initializing FAMI...')  
#This function will wish you as per current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <=12:
        speak('Good Morning' + MASTER)
    elif hour>=12 and hour<=18:
        speak('Good Afternoon'+ MASTER)
    else:
        speak('Good Evening'+ MASTER)   
    #speak('I am FAMI.. How may i help you?')         
#main program start from here
#wishMe()  
#this function will take command from microphone
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        #speak('Listening...')
        r.phrase_threshold= 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio= r.listen(source)
    try:
        #print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in' ) 
        print(f'user said:{query}\n')
    except sr.UnknownValueError:#Exception as e:
        #print('Sir you there') 
        query= takeCommand();  #query =None #myCommand(takeCommand())#None
    return query      
query = takeCommand() 
def myCommand(query):
#logic for executing task as per the query
    if 'there' in query.lower():
        speak('For you always sir')
    elif 'meaning' in query.lower():
        speak('FAMI is the acronym of Future Acknowledge Me as Invincibles') #The first super bot of SAM INDUSTRIES #email: samindustries404@gmail.com

        
    elif 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences=3)
        print(results)
        speak(results)

    elif 'youtube' in query.lower():
        speak('On your command sir') 
        open_youtube = webbrowser.get('windows-default').open('https://youtube.com')
        #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
    elif 'google' in query.lower():
        #webbrowser.open('youtube.com') 
        
        open_google = webbrowser.get('windows-default').open('https://google.com')
        time.sleep(5)
        print(pyautogui.position())
        pyautogui.doubleClick(420,64)
        time.sleep(5)
        pyautogui.typewrite(['backspace'])
        pyautogui.typewrite(['backspace'])
        
        test= query.split() #split function will split the sentance into single word
        pyautogui.typewrite(str(test[2]))
        time.sleep(7)
        pyautogui.typewrite(['enter'])

    elif 'open youtube' in query.lower(): 
        open_youtube = webbrowser.get('windows-default').open('https://youtube.com')
        
    elif 'music' in query.lower():
        speak('On your command sir') 
        songs_dir='E:\\Eminem\\(2003) Eminem - Straight From the Lab'
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    elif 'time' in query.lower():
        strTime= datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'{MASTER} the time is{strTime}')

    elif 'visual' in query.lower(): #to open visual studio
        codePath= 'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codePath)

myCommand(query)



while True:
    myCommand(takeCommand())