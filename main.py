import speech_recognition as sr
import pyttsx3 as pt
import activity
import  random

class AmbientNoise:
    def __init__(self):
        try:
            with sr.Microphone() as source:
                sr.Recognizer().adjust_for_ambient_noise(source)
                sr.Recognizer().energy_threshold
        except:
            print("error occurred in ambient try")

class Recognizer:
    requestList = ["anything else ?", "is there anything else for me ?"]
    def take_command(name):
        AmbientNoise()
        recognize = sr.Recognizer()
        text = "hello,"+name+" what can i do for you?"
        Recognizer.Speak(text)
        firstTime = True
        runAgain = True
        with sr.Microphone() as source:
            while runAgain:
                if firstTime is False:
                    Recognizer.Speak(random.choice(Recognizer.requestList))
                firstTime = False
                recognize.pause_threshold = 0.9
                audio = recognize.listen(source)
                validity = recognize.recognize_google(audio)
                print(validity)
                if "no" in validity.split() or 'not' in validity.split() or 'nothing' in validity.split():
                    Recognizer.Speak("Okay, shutting down myself. Have a nice day")
                    runAgain = False
                    break

                try:
                    request = recognize.recognize_google(audio)
                    print("request: "+request)
                    response = activity.Activities().activityManger(request)
                    print("response: "+response)
                    Recognizer.Speak(response)
                except Exception as e:
                    Recognizer.Speak("sorry say that again")
                    Recognizer.take_command("")

    def Speak(textToSpeech):
        engine = pt.init()
        engine.say(textToSpeech)
        engine.runAndWait()

    def get_name(number):
        AmbientNoise()
        Recognizer.Speak("Hey! What's your name?")
        take_name = sr.Recognizer()
        nametext = ""
        with sr.Microphone() as source:
            take_name.pause_threshold = 0.5
            name = take_name.listen(source)
            try:
                nametext = take_name.recognize_google(name)
            except Exception as e:
                print("exception")
                print(e)
                Recognizer.Speak("Sorry")
                Recognizer.get_name(number)
        return nametext
if __name__ == '__main__':
    Recognizer.take_command(Recognizer.get_name("one"))