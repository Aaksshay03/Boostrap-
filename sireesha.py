import speech_recongition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.int()
voices=engine.getproperty('voices')
engine.setproperty('voice',voices[1].id)
recognizer=sr.Recorgnizer()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises...Please wait')
        recognizer.adjust_for_ambident_noise(source,duration=0.5)
        print('Ask me anything..')
        recordedaudio=recognizer.listen(source)
        
        try:
            command=recognizer.recognize_google(recordedaudio,lang)
            
    if 'chrome' in command:
            a='Opening chrome..'
            engine.say(a)
            engine.runAndWait()
            program="C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([program])
            
    if 'time' in command:
            time=datetime.datetime.now().strftime('%I:%M%p')
            print(time)
            engine.say(time)
            engine.runAndWait()
            
     if 'play' in command:
            b='Opening Youtube'
            engine.say(b)
            engine.runAndWait()
            pywhatkit.playonyt(command)
