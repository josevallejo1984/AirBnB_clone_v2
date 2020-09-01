#!/usr/bin/python3
"""Start a new server using flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Route
    Returns:
        route: html static
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run()
