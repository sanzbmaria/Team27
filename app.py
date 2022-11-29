import datetime
from flask import Flask, render_template

app = Flask(__name__)


class User:
    name = "Jane Doe"
    major = "Software"


user = User


@app.route("/")
def hello():
    return render_template("index.html", user=user)
