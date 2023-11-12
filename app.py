# Open Terminal in your virtual environment and run
# python -m pip install flask
# This will allow app.py to be run on the server

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/", methods=["GET", "POST"])
@cross_origin()
def home():
    testVar = ""

    if request.method == "POST":
        testVar = request.get_json()
        return request.get_json()

    if request.method == "GET":
        return testVar

    return "Hello World!"


app.run()
