"""Flask application factory and blueprint registration."""

from flask import Flask
from application.bp.homepage.homepage import homepage


def create_app():
    """Create and configure the Flask app."""
    app = Flask(__name__)
    app.register_blueprint(homepage, url_prefix="/")
    return app


def init_app():
    """Entry point used by tests."""
    return create_app()


app = init_app()

