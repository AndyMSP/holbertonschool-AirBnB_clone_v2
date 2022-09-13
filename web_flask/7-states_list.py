#!/usr/bin/python3
"""Starts a basic flask web application"""

from flask import Flask, render_template
from markupsafe import escape

from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def hello_hbnb():
    """Function to run when '/states_list' is accessed"""
    states = [state for state in storage.all(State).values()]
    states.sort(reverse=False, key=lambda state: state.name)
    return (render_template('7-states_list.html', states=states))


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=False)
