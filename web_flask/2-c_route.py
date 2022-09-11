#!/usr/bin/python3
"""Starts a basic flask web application"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Function to run when '/' is accessed"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function to run when '/hbnb' is accessed"""
    return ("HBNB")


@app.route("/c/<text>")
def c_text(text):
    """Function to run when '/c/<text>' is accessed"""
    return ("C {}".format(text.replace('_', ' ')))


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=False)
