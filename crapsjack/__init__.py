from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app(base_dir: str):
    app = Flask(__name__, template_folder=base_dir + '/templates')
    app.config.from_object(Config)
    # Initialize Plugins
    db.init_app(app)
    from crapsjack.models import User
    migrate.init_app(app, db)

    with app.app_context():
        from . import views
        from . import auth

        # Register Blueprints
        app.register_blueprint(views.main_blueprint)

    return app
