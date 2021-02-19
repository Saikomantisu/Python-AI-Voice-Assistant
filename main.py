import os
import random
from gtts import gTTS
import webbrowser
import playsound
import time
import speech_recognition as sr

r = sr.Recognizer()

def gtts(text):
    ran = random.randint(1, 100000)
    file = "audio-" + str(ran) + ".mp3"
    tts = gTTS(text, lang='en')
    tts.save(file)
    print(text)
    playsound.playsound(file)
    os.remove(file)

def respond(voice_data):
    if 'exit' in voice_data:
        exit()

    if 'what is the time' in voice_data:
        gtts(time.ctime())
    
    if 'who are you' in voice_data:
        gtts("I am an Artificial intelligence")

    if 'what is your name' in voice_data:
        gtts("My name is Eva")

    if 'how are you' in voice_data:
        gtts("I,m GOOD!")

    if 'who built you' in voice_data:
        gtts("My developer is HeX-006")

    if 'search' in voice_data:
        gtts("What you want to search?")
        search = audio_record()
        url = f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        gtts("This is what i found about " + search  + "on internet")

def audio_record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            gtts("sorry, I didn't get that")
        except sr.RequestError:
            gtts("sorry, my speech service is DOWN")
        return voice_data

time.sleep(1)
gtts("How Can I Help You")
while 1:
    voice_data = audio_record()
    respond(voice_data)