from flask import Flask, jsonify
from utils import db
from config import DevConfig
from cat_bluerprint import cat_bp

app = Flask(__name__)
app.config.from_object(DevConfig)


db.init_app(app)

app.register_blueprint(cat_bp, url_prefix="/cats")


@app.get("/")
def index():
    return jsonify({"message": "'Hello World"})
