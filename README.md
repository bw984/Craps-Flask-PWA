# Craps-Flask-PWA
Full web app version of bwcraps with database and user bankroll tracking

## Flask Command Line Workflow

export FLASK_APP=app

db init

from app import db
db.create_all()  # creates tables for all models

flask db migrate -m"message here"

flask db upgrade