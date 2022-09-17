import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','secret')



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" +os.path.join(BASE_DIR,'cats.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


uri =  os.getenv('DATABASE_URI')
print(uri)

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=uri
    SQLALCHEMY_TRACK_MODIFICATIONS=False



config_vars={
    'dev': DevConfig,
    'prod':ProdConfig
}