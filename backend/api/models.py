from api import db


class User(db.Model):
    __tablename__ = 'users'

    identikey = db.Column(db.String(8), primary_key=True)
    session = db.PickleType()

    def __init__(self, identikey: str):
        self.identikey = identikey

    def save(self):
        db.session.add(self)
        db.session.commit()
