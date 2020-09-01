#!/usr/bin/python3
"""Start a new server using flask"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def route_number(n):
    """Route number

    Args:
        n (int): inter value convert
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def route_template(n):
    """Route template

    Args:
        n (int): inter value recive from render_template

    Returns:
        html: static html from template
    """
    return render_template('5-number.html', name=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def route_template_two(n):
    """Route template two

    Args:
        n (int): inter value recive from render_template

    Returns:
        html: static html from template
    """
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
