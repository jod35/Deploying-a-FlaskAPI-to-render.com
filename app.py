from flask import Flask, jsonify
from utils import db
from config import DevConfig, ProdConfig
from cat_bluerprint import cat_bp
from models import Cat


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(cat_bp, url_prefix="/cats")

    @app.shell_context_processor
    def make_shell_context():
        return{
            'db':db,
            'Cat':Cat
        }


    return app
