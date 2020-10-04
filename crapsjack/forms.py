from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Display Name:')
    email = StringField('Email Address:')
    submit = SubmitField('Register')


class DelForm(FlaskForm):

    id = IntegerField('Id Number of User to Remove:')
    submit = SubmitField('Remove User')
