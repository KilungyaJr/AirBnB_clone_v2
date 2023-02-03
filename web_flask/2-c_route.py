#!/usr/bin/python3
"""
Flask web application script
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Route function for the index page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route function for the /hbnb page
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """
    Route function for the /c/<text> page
    """
    text = text.replace("_", " ")
    return "C " + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
