import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine =  pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        pass
    return command

def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song, use_api=True)

        elif 'time' in command:
            time = dt.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('The Current time is ' + time)

        elif 'date' in command:
            date = dt.datetime.now().strftime('%A %B %dth of %Y')
            print(date)
            talk('The Current Date is ' + date)
        elif 'day' in command:

            day = dt.datetime.now().strftime('%A')
            print(day)
            talk('Today is ' + day)

        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'what was' in command:
            event = command.replace('what was', '')
            info = wikipedia.summary(event, 1)
            print(info)
            talk(info)
        elif 'what is' in command:
            event = command.replace('what is', '')
            info = wikipedia.summary(event, 1)
            print(info)
            talk(info)

        elif 'joke' in command:
            talk(pyjokes.get_joke())

        else:
            talk("I'm Sorry. Abraham hasn't programmed that into me yet")


while True:
    run_alexa()