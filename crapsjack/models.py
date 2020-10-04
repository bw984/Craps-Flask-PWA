from crapsjack import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    lifetime_earnings = db.Column(db.FLOAT)
    session_earnings = db.Column(db.FLOAT)
    lifetime_rolls = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username
