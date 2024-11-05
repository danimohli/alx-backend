#!/usr/bin/evn python3
"""
Basic Flask application with a single route.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        The HTML template for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
