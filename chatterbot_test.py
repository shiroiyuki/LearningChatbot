# -*- coding: utf-8 -*-
import nltk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def main(words):
    bot = ChatBot("bot")
    bot.set_trainer(ChatterBotCorpusTrainer)
    bot.train("chatterbot.corpus.chinese") 
    try:
        result = bot.get_response(words)   
        return "科蘿娜: "+ str(result)
    except Exception as e:
        print(str(e))
    return bot

if __name__ == '__main__':
    user = input("請輸入你的名子：")
    main(user)
