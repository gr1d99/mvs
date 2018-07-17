"""Application entry-point"""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.authentication import authentication_app
from config import ENVIRONMENT_OBJECT

APP = Flask(__name__)
APP.config.from_object(ENVIRONMENT_OBJECT)
APP.register_blueprint(
    authentication_app,
    url_prefix='/auth'
)
BCRYPT = Bcrypt(APP)
DB = SQLAlchemy(APP)

if __name__ == '__main__':
    APP.run()
