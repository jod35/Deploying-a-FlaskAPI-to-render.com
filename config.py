import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','secret')



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" +os.path.join(BASE_DIR,'cats.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False