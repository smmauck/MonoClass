from api import db


class User(db.Model):
    __tablename__ = 'users'

    identikey = db.Column(db.String(8), primary_key=True)
    session = db.Column(db.PickleType(), nullable=False)

    def __init__(self, identikey: str):
        self.identikey = identikey

    def save(self):
        if User.query.get(self.identikey) is None:
            db.session.add(self)
        else:
            User.query.get(self.identikey).session = self.session

        db.session.commit()
