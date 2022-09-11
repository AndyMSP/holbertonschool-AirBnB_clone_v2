#!/usr/bin/python3
"""Starts a basic flask web application"""

from flask import Flask, render_template
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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function to run when '/c/<text>' is accessed"""
    return ("C {}".format(text.replace('_', ' ')))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Function to run when /python/<text>' is accessed"""
    return("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_page(n):
    """Function to run when '/number_template/<n>' is accessed"""
    return (render_template('5-number.html', number=n))


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=False)
