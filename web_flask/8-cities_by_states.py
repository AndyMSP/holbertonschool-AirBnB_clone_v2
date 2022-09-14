#!/usr/bin/python3
"""Starts a basic flask web application"""

from flask import Flask, render_template
from markupsafe import escape

from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """procedure to run after request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Function to run when '/states_list' is accessed"""
    states = [state for state in storage.all(State).values()]
    states.sort(reverse=False, key=lambda state: state.name)
    return (render_template('7-states_list.html', states=states))


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_statesb():
    """Function to run when '/cities_by_states' is accessed"""
    states = storage.all(State).values()
    return (render_template('8-cities_by_states.html', states=states))


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=False)
