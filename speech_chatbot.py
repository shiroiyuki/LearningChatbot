# -*- coding: utf-8 -*-
import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def recognize(audio):
    try:
        return r.recognize_google(audio, language='zh-TW')
    except:
        return ''

bot = ChatBot("bot")
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.chinese")
bot.train("chatterbot.corpus.chinese.greetings")

name = input("請輸入你的名子:")
if __name__ == "__main__":
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source: r.adjust_for_ambient_noise(source)
        print(r.energy_threshold) 
        while True:
            with sr.Microphone() as source:
                #print("please say something")
                audio = r.listen(source)
            try:
                #print("compute")
                words = r.recognize_google(audio, language='zh-TW')
                print(name + ":" + words)
            except sr.UnkonownValueError:
                print("Didn't catch")
                continue
            except sr.RequestError as e:
                print(str(e))
                continue
            except:
                print("Unknown error!")
                continue
           # print("find  responsed")
            result = bot.get_response(words)
            print("機器人:" + str(result))
    except Exception as e:
        print(str(e))
