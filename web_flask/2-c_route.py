#!/usr/bin/python3
"""
Start my framework application
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Message to index application"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """returns a parameter by url as string"""
    txt = text.replace('_', ' ')
    return "C {}".format(escape(txt))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
