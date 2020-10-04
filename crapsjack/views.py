from flask import Blueprint, redirect, url_for, render_template
from crapsjack.forms import AddForm, DelForm
from crapsjack.models import User
from crapsjack import db

craps_jack_blueprint = Blueprint('main', __name__)


@craps_jack_blueprint.route('/')
def home():
    return render_template('index.html')


@craps_jack_blueprint.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Add new User to database
        new_user = User(username=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.list_users'))

    return render_template('add.html', form=form)


@craps_jack_blueprint.route('/list_users')
def list_users():
    # Grab a list of users from database.
    users = User.query.all()
    return render_template('list.html', users=users)


@craps_jack_blueprint.route('/delete_user', methods=['GET', 'POST'])
def delete_user():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('main.list_users'))
    return render_template('delete.html', form=form)
