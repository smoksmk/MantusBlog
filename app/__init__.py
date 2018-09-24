from flask import Flask
from . import config
from api.v1.view import post_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(post_bp, url_prefix='/v1/')

    return app