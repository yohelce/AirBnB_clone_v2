#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Print first message in HTML """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns a string at the /hbnb/ route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Returns string at the /c/<text> route,
    expands the <text> variable"""
    text_add = text.replace('_', ' ')
    return 'C {}'.format(text_add)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Returns a string at the /python route, with a default text
    of 'is cool', or the expansion of <text>"""
    text_add = text.replace('_', ' ')
    return 'Python {text_add}'.format(text_add)


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """ Returns a string at the /number/<n> route only
    if n is a integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Returns a template at the /number_template/<n> route,
    expanding route"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ Returns a template at the /number_odd_or_even/<n>
    route, display if the number is odd or even """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)