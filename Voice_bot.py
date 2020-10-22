import requests
import speech_recognition as sr
from gtts import gTTS

import playsound
import os

bot_message = ""
message=""

...

while bot_message != "Bye" or bot_message != "thanks":

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening: ")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("You Said: {}".format(message))

        except:
            print("Unable to recognise your voice,  please repeat")
    if len(message)==0:
        continue

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})



    print("Chatbot says: ",end = ' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    myobj.save("welcome.mp3")

    playsound.playsound("welcome.mp3")
    os.remove("welcome.mp3")


# need to use pocket sphinx for offline speech to text

  


