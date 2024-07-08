from flask import Flask

newApp = Flask(__name__)


@newApp.route("/")
def home():
    return "It's just a webpage. Hello World!"


"""
This is just a simple webpage that displays the above string using flask.
It will be used as the application for all of the different development tools used in this
project. 
"""