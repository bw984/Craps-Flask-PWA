from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()


def create_app(base_dir: str):
    app = Flask(__name__, template_folder=base_dir + '/templates')
    app.config.from_object(Config)
    db.init_app(app)
    from crapsjack.models import User
    migrate.init_app(app, db)

    from crapsjack.views import craps_jack_blueprint
    app.register_blueprint(craps_jack_blueprint)

    return app
