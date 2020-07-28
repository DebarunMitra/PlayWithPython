import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime


r = sr.Recognizer()
#speak(sr.Microphone.list_microphone_names())

def record_audio(ask = ''):
    with sr.Microphone() as source:
        if ask != '':
            speak(ask)
        r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold()
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I could not recognize you :(")
        except sr.RequestError:
            speak("Sorry, My service is down :(")
        return voice_data


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    #speak(f"kiri: {audio_string}")  # speak what app said
    os.remove(audio_file)  # remove audio file

def process_voice(voice):
    if 'hello' in voice:
        speak('Hi, I am Seri...')
    if 'what is the time' in voice:
        speak(ctime())
    if 'search' in voice:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for '+ search)
    if 'find location' in voice:
        location = record_audio('Please, tell me the place...')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    if 'exit' in voice:
        speak('Goodbye')
        exit()


time.sleep(1)
speak("How can I help you... ")

while 1:
    voice_data = record_audio()
    process_voice(voice_data)
