#!/usr/bin/env python3
"""
Basic Flask application with Babel for language support and translation.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


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

SUPPORTED_LOCALES = ['en', 'fr', 'es']


@babel.localeselector
def get_locale():
    locale_arg = request.args.get('locale')

    if locale_arg and locale_arg in SUPPORTED_LOCALES:
        return locale_arg

    return request.accept_languages.best_match(SUPPORTED_LOCALES)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages based on
    request headers.

    Returns:
        str: The best matching language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page with translations for title and header.

    Returns:
        The HTML template for the index page.
    """
    return render_template('3-index.html',
                           title=_("home_title"), header=_("home_header"))


if __name__ == '__main__':
    app.run()
