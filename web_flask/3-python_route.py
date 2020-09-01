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

# For handle var in the route must be inside <my_var>
@app.route('/c/<text>', strict_slashes=False)
def route_c(text):
    """Route C
    Args:
        text (str): var given for url
    Returns:
        html: static web page
    """
    return 'C' + ' ' + text.replace('_', ' ')

# One route for python lonly and other for add var to route
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def route_python(text='is cool'):
    """Route Python
    Args:
        text (str): var given for url
    Returns:
        html: static web page
    """
    return 'Python' + ' ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
