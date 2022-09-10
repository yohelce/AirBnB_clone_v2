#!/usr/bin/python3
""" Module Hello route of Flask """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Print first message in HTML """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns a string at the /hbnb/ route """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
