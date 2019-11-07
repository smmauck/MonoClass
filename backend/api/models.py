from api import db


class User(db.Model):
    __tablename__ = 'users'

    identikey = db.Column(db.String(8), primary_key=True)
