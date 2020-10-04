from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from crapsjack import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    lifetime_earnings = db.Column(db.FLOAT)
    session_earnings = db.Column(db.FLOAT)
    lifetime_rolls = db.Column(db.Integer)

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username
