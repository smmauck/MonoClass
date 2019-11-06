from os import environ

class Config:

    # General config
    DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = b'\xdaS1H\xd7PRi\xad\xcf`O\x94\xdf\xba9u\xfby\xdb\xf90=\x9e'

    # Database config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False