#!/usr/bin/python3
"""
Flask web application script
listening on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
"""

from flask import Flask, render_template

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
def c(text):
    """Route for the C page."""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route('/python/<text>')
def python(text="is cool"):
    """Route for the Python page."""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    """Route for the number page."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Route for the number template page."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
