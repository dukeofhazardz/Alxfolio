#!/usr/bin/python3

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return render_template("home.html")

@app.route("/signup", strict_slashes=False)
def signup():
    return render_template("signup.html")

@app.route("/login", strict_slashes=False)
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)