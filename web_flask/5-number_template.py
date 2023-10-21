#!/usr/bin/python3
"""
5-number_template module
"""
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Route to display Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route to display C followed by the value at text"""
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route to display Python followed by value at text
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Route to display a number
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route to display a html page if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
