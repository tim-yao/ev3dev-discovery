#!/usr/bin/env python3

# SSH into ev3 then run `env FLASK_APP=app.py flask run --host=0.0.0.0 --port=8000`
# Then we can access it by ev3 ip like http://192.168.2.2:8000/
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
