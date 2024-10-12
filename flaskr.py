#! /usr/bin/python3.13
"""
this is a blog app created through the Flask documentation to learn the basics
of the Flask application and to practice my touch-typing (lol)
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
