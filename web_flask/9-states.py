#!/usr/bin/python3
"""Starts a basic flask web application"""

from flask import Flask, render_template, redirect
from markupsafe import escape

from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
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


@app.route("/states", strict_slashes=False, defaults={'id': None})
@app.route("/states/<id>", strict_slashes=False)
def states_dynamic(id=id):
    """Function to run when '/states' or 'states/<id>' is accessed"""
    states = storage.all(State).values()
    valid_ids = [state.id for state in states]
    if id is None:
        title = 'States'
        states = states
        flag = 'States'
    elif id in valid_ids:
        states = [state for state in states if state.id == id]
        title = 'State : {}'.format(states[0].name)
        flag = 'State'
    else:
        title = 'Not Found!'
        states = []
        flag = 'empty'
    return render_template(
        '9-states.html',
        title=title,
        states=states,
        flag=flag
        )


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True)
