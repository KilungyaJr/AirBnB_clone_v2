#!/usr/bin/python3
"""
Flask web application script
"""

from flask import Flask, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Route function for the index page
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    Route function for the /hbnb page
    """
    return "HBNB"


@app.route('/c/<text>')
def display_text(text):
    """
    Route function for the /c/<text> page
    """
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python")
@app.route('/python/<text>')
def display_python(text='is cool'):
    """
    Route function for the /python/<text> page
    """
    text = text.replace("_", " ")
    return "Python " + text


@app.route('/number/<int:n>')
def number(n):
    """Return 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
