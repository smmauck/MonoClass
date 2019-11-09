from os import environ


class Config:

    # General config
    DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = b'\xdaS1H\xd7PRi\xad\xcf`O\x94\xdf\xba9u\xfby\xdb\xf90=\x9e'

    # Database config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT config
    JWT_SECRET_KEY = b'\xca\xb0<\xc8S\xfc\x01v=\xbb\x08lo\x96\xb0{\xb4\xca\xc9`\xf4-\xffB'
