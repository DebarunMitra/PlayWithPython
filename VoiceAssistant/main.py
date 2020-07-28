import speech_recognition as sr
import webbrowser
from time import ctime
import time
import playsound
import os


r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())

def record_audio(ask = ''):
    with sr.Microphone() as source:
        if ask != '':
            print(ask)
        r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold()
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I could not recognize you :(")
        except sr.RequestError:
            print("Sorry, My service is down :(")
        return voice_data

def process_voice(voice):
    if 'hello' in voice:
        print('Hi, I am Sari...')
    if 'what is the time' in voice:
        print(ctime())
    if 'search' in voice:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for '+ search)
    if 'find location' in voice:
        location = record_audio('Please, tell me the place...')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
    if 'exit' in voice:
        print('Goodbye!!')
        exit()


time.sleep(1)
print("How can I help you... ")

while 1:
    voice_data = record_audio()
    process_voice(voice_data)
