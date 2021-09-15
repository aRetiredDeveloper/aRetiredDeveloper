import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    basedir = os.path.abspath(os.path.dirname(__file__))
