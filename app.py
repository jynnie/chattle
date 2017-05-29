from flask import Flask
from flask import flash, render_template, request, session, abort, redirect

#import os
import datetime
#from sqlalchemy.orm import sessionmaker
#from wtforms import Form, TextField, validators, StringField, SubmitField
#from tabledef import *

#engine = create_engine('sqlite:///messages.db', echo=True)

app = Flask(__name__)
#app.config.from_object(__name__)

messages = []

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html',
                        messages = messages)

@app.route("/message")
def message():
    a = request.args.get('say')
    if a != None:
        messages.append([datetime.datetime.now().time(), a])
    return redirect("/")

if __name__ == "__main__":
    #app.secret_key = os.urandom(12)
    app.run(debug=True)
