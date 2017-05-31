#coding=utf-8
from flask import *
import os
app = Flask("todo-list")
app.debug = True
app.static_folder = 'static'

@app.route("/")
def echo():
    return render_template("lab4.html")

@app.route("/whoareyou",methods=["GET","POST"])
def whoareyou():
    if request.method == "POST":
        name = request.form.get("name")
        if name is not "":
            return render_template("chat.html",name=name)       
        else:
            return render_template("chat.html")
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