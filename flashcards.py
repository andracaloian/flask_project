from flask import Flask
from datetime import datetime

app = Flask(__name__) #calls the flask constructor which creates a global flask app obj

@app.route("/") #changes from a simple function into a view function; a decorator
def welcome():
    return 'Welcome to my Flash Cards application!'

@app.route("/date")
def date():
    return 'This page was served at ' + str(datetime.now())

#add a page that shows how many times it has been viewed
counter=0
@app.route("/count_views")
def count_views():
    global counter
    counter+=1
    return 'This page was serverd ' + str(counter) + ' times'