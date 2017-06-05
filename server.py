#coding=utf-8
data = ['','','','','','','','','','']
from flask import *
import os
import nltk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask("todo-list")
app.debug = True
app.static_folder = 'static'
bot = ChatBot("bot")
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.chinese")
response = ""
result = ""
print("hi")
@app.route("/")
def echo():
    return render_template("lab4.html")

@app.route("/whoareyou",methods=["GET","POST"])
def whoareyou():
    if request.method == "POST":
        name = request.form.get("name")
        if name is not "":
            for i in xrange(0,6) :
                data[i] = data[i+1]
            try:
                result = bot.get_response(name)   
                response = "科蘿娜: "+ str(result)
            except Exception as e:  
                print(str(e))
                reponse = ""
            data[6] = data[8]
            data[7] = data[9]
            data[8] = name
            data[9] = response
            return render_template("chat.html",name = data)       
        else:
            return render_template("chat.html",name = data)
    if request.method == "GET":
        return render_template("chat.html")

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
    if filename:
        file_path = os.path.join(app.root_path, endpoint, filename)
        values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)

if __name__ == "__main__":
    app.run(port=80)
