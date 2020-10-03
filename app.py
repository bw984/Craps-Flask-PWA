from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    return 'Hello World CrapsJack! Now on Azure!'

"""
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000')
"""