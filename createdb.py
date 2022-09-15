from utils import db
from models import Cat
from app import app

with app.app_context():
    db.create_all()
