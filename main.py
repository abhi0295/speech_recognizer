


import pyttsx3
import speech_recognition as sr
import os
import pyttsx3 as pt
import webbrowser
class Recognizer:
    def take_command(name):
        recognize = sr.Recognizer()
        text = "hello, ",name," what can i do for you?"
        with sr.Microphone() as source:
            Recognizer.Speak(text)
            recognize.pause_threshold = 0.7
            audio = recognize.listen(source)

            try:
                query  = recognize.recognize_google(audio)
                new_text = "Are you saying "+query
                Recognizer.Speak(new_text)
            except Exception as e:
                Recognizer.Speak("sorry say that again")
                Recognizer.take_command("")


    def Speak(textToSpeech):
        engine = pyttsx3.init()
        engine.say(textToSpeech)
        engine.runAndWait()

    def get_name(number):
        Recognizer.Speak("Hey! What's your name?")
        take_name = sr.Recognizer()
        nametext = ""
        with sr.Microphone() as source:
            take_name.pause_threshold = 0.5
            name = take_name.listen(source)
            try:
                nametext = take_name.recognize_google(name)
                print("printing name "+nametext)
            except Exception as e:
                print("exception")
                print(e)
                Recognizer.Speak("Sorry")
                Recognizer.get_name(number)
        return nametext
if __name__ == '__main__':
    print("Start")
    Recognizer.take_command(Recognizer.get_name("one"))

