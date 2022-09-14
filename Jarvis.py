import pyttsx3
import speech_recognition as sr
import datetime
import time
import wikipedia
import webbrowser
import os
import smtplib
import random
import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amrit25092000@gmail.com', 'Amrit@123')
    server.sendmail('amrit25092000@gmail.com', to, content)
    server.close()

def sendMessage():
    def send_sms(number, message):
        url =  "https://www.fast2sms.com/dev/bulkV2"
        params = {
            "authorization": 'hEUAoQ1KOXMaxlLRSfm2H43gDCbTJ8pBsWeidYnq75wz96uyZj8k6OR5IoMYjXrihPSZq7E0BQyN1ACL',
            "sender_id": "TXTIND",
            "message": message,
            "language": 'english',
            "route": 'v3',
            "numbers": number
        }

        response = requests.get(url, params=params)
        a = response.json()
        #print(a)
        return a.get("return")

    #send_sms("9479675739", "Hello Nikhil")


    def btnClick():
        num = textNumber.get()
        msg = textMsg.get("1.0",END)
        r = send_sms(num, msg)
        if r:
            showinfo("send success", "Sent successfully")
        else:
            showerror("Error", "Something went wrong")

    root = Tk()
    root.title("Message sender")
    root.geometry("400x550")
    font = ("Helvetica", 22, "bold")
    textNumber = Entry(root, font = font)
    textNumber.pack(fill = X, pady=20)
    textMsg = Text(root)
    textMsg.pack(fill=X, pady=10)
    sendBtn = Button(root,text="Send SMS", command=btnClick)
    sendBtn.pack()
    root.mainloop()


    
if __name__=="__main__":
    wishMe()
    #if 1:
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            music_dir = 'C:\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'reminder' in query:
            speak("What shall I remind you about sir?")
            text = takeCommand()
            speak('In how many minutes sir?')
            local_time = int(takeCommand())
            local_time = local_time * 60
            speak("The reminder is set sir. I'll remind you about the same.")
            time.sleep(local_time)
            speak(text * 3)

        elif 'set an alarm' in query:
            speak('In how many minutes sir?')
            local_time = int(takeCommand())
            local_time = local_time * 60
            speak("The alarm is set sir")
            time.sleep(local_time)
            music_dir = 'C:\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'open vs code' in query:
            codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open calculator' in query:
            codepath = "C:\\Users\\Dell\\Downloads\\Calculator.exe"
            os.startfile(codepath)

        elif 'send message' in query:
            sendMessage()

        elif 'email to nikhil' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "advaninikhil19@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry Sir! I am not able to send this email at the moment")

        elif 'email to piyush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vermapiyush0411@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry Sir! I am not able to send this email at the moment")

        elif 'email to kunal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kunaladvani29@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry Sir! I am not able to send this email at the moment")

        elif 'hello jarvis' in query:
            speak('Hello sir! Welcome back.')

        elif 'are you up' in query:
            speak('For you sir, always')

        elif 'how are you' in query:
            speak('I am absolutely fine sir. Thank you for asking!')

        elif 'go outside' in query:
            speak('You shouldn\'t go outside sir,its not safe. Stay inside and stay safe')

        elif 'how\'s the weather outside' in query:
            speak('Its a hot day sir!')

        elif 'thank you' in query:
            speak("You are most welcome sir")

        elif 'quit' in query:
            speak('Thank you for your time sir! Hope to see you soon')
            quit()

        
        




            

