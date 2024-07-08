from flask import Flask

newApp = Flask(__name__)


@newApp.route("/")
def home():
    return "It's just a webpage. Hello World!"


if __name__ == "__main__":
    newApp.run(debug=True, port=8080, host="0.0.0.0")
    # flask's default port is 5000 so mapped to port 8080 and listen all ports with 0.0.0.0

"""
This is just a simple webpage that displays the above string using flask.
It will be used as the application for all of the different development tools used in this
project. 
"""
