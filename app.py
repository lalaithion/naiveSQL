#!/usr/bin/env python3

from flask import Flask, render_template, request
import v1

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('index.html',
            valid=1)
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def account():
    username = request.form['username']
    password = request.form['password']
    if v1.validate(username, password):
        return render_template('account.html',
                username=username, password=password)
    else:
        return render_template('index.html',
                valid=0)

if __name__ == "__main__":
    app.run()
