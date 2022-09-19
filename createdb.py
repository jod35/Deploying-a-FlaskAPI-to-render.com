from utils import db
from models import Cat
from app import create_app
from config import config_vars

app=create_app(config_vars['prod'])

with app.app_context():
    db.create_all()
