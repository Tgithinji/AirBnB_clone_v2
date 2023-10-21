#!/usr/bin/python3
"""
1-hello_route module
"""
from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
