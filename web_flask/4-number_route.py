#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/C/<text>', strict_slashes=False)
def CText(text):
    textC = text.replace("_", " ")
    return ("C {}".format(textC))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    textC = text.replace("_", " ")
    return ("Python {}".format(textC))


@app.route('/number/<int:n>', strict_slashes=False)
def numberText(n):
    return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
