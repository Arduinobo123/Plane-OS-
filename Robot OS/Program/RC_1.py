import pyttsx3
import smtplib
import random
import datetime
import os
import sys
from time import sleep
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer 1: ' + audio)
    engine.say(audio)
    engine.runAndWait()

speak("This is co-pilot, computer 1")
