#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/pythontest')
def hello_world():
    return 'Hello, World!'

app.run()
