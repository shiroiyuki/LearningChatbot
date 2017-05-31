# -*- coding: utf-8 -*-
import speech_recognition as sr
import nltk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS 

def recognize(audio):
    try:
        return r.recognize_google(audio, language='zh-TW')
    except:
        return ''


def  main(name):
    bot = ChatBot("bot")
    bot.set_trainer(ChatterBotCorpusTrainer)
    bot.train("chatterbot.corpus.chinese") 
    while True:
        words = input(name + ": ")
        try:
            result = bot.get_response(words)
            print("科蘿娜: ",result)
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    user = input("請輸入你的名子：")
    main(user)
