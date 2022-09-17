from app import create_app
from config import config_vars


app= create_app(config_vars['prod'])