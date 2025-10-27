from flask import Flask
from application.bp.homepage.homepage import homepage

def create_app():
    app = Flask(__name__)
    app.register_blueprint(homepage, url_prefix="/")
    return app

# what the tests import
def init_app():
    return create_app()

# runtime entrypoint
app = init_app()
