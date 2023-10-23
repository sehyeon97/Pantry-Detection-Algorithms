# Open Terminal in your virtual environment and run
# python -m pip install flask
# This will allow app.py to be run on the server

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"
