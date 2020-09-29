import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour >=12 and hour<17:
        speak("Good Afternoon Sir!")

    elif hour >=17 and hour<21:
        speak("Good Evening Sir!")

    else:
        speak("Good Night Sir. Its time to sleep. Sweet dreams!")

    speak("I am Jarvis. I have worked with Iron Man and I am fortunate enough to  work with you too Sir ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1.0
        audio = r.listen(source)

    try:
        print("Recognizing.....")
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
    server.login('putyourgmailidhere', 'putyourpasswordhere')
    server.sendmail('putyourgmailidhere', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    
    #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")

    elif 'play music' in query:
        music_dir = 'C:\\Users\\shubh\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to harry' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "singhvineet1374@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")


        except Exception as e:
            print(e)
            speak("Sorry!, but the email could not be sent")

    elif 'open camera roll' in query:
        codePath = "C:\\Users\\shubh\\Pictures\\Camera Roll"
        os.startfile(codePath)






