import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)


print(r.recognize_google(audio, language = 'zh-TW'))
