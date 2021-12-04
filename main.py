import os
import pyttsx3
import speech_recognition as sr
import datetime
import boto3
import pyaudio
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening voice input')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print('Recognizing voice input..')
        cmd_input = r.recognize_google(audio)
        return cmd_input
    except Exception as e:
        print(e)
        speak('Give the voice input again')
        return None


print('here the code begins')
speak('Here the code Begins')
print('Give your command')
speak('Give you command')
output = command()
print(output)


