#!/usr/bin/env python3
"""
Basic Flask application with Babel for language support.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask app.
    Sets available languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Render the index page.
    Returns:
        The HTML template for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=False)
