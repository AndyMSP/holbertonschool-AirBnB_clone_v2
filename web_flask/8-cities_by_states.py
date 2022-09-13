#!/usr/bin/python3
"""Starts a basic flask web application"""

from flask import Flask, render_template
from markupsafe import escape

from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def hello_hbnb():
    """Function to run when '/cities_by_states' is accessed"""
    states = storage.all(State).values()
    page = render_template('8-cities_by_states.html', states=states)
    storage.close()
    return(page)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=False)
