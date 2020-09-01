#!/usr/bin/python3
"""Start a new server using flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route_home():
    """Route home
    Returns:
        route: html static
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def route_hbnb():
    """Route hbnb
    Returns:
        route: html static
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
