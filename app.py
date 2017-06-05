from flask import Flask
from flask import render_template, request, session, abort, redirect

import os #used to create a random key for secret_key
import datetime #module that can get date time of now (and formats)

app = Flask(__name__)
app.config.from_object(__name__)

messages = []

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html',
                        messages = messages)

@app.route("/user")
def user():
    a = request.args.get('name') #gets the submitted value
    if a != None: #if not an empty name
        session['logged_in'] = True #says you are logged in
        session['name'] = a #sets user name for the session
    return redirect("/")

@app.route("/message")
def message():
    a = request.args.get('say') #gets the submitted value of the message
    if a != None: #if not an empty message
        messages.append([datetime.datetime.now().strftime("(%x %X)"), session.get('name'), a]) #add message with time, user, and message to the list
    return redirect("/")

@app.route("/delete")
def delete():
    m = int(request.args.get('m')) #gets the index value of the message
    del messages[m] #deletes the message at that index
    return redirect("/")

if __name__ == "__main__":
    app.secret_key = os.urandom(12) #required in order to create a session
    app.run(debug=True, host='0.0.0.0', port=80) #putting it on this port and host allows it to be seen from IP address
