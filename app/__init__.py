"""Application entry-point"""

from flask import Flask, render_template
from flask.views import View
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import ENVIRONMENT_OBJECT

APP = Flask(__name__)
APP.config.from_object(ENVIRONMENT_OBJECT)

BCRYPT = Bcrypt(APP)
DB = SQLAlchemy(APP)
JWT = JWTManager(APP)
migrate = Migrate(APP, DB)


from app.authentication import AUTHENTICATION_APP


APP.register_blueprint(
    AUTHENTICATION_APP,
    url_prefix='/auth'
)


class IndexView(View):
    methods = ['GET', ]

    def dispatch_request(self):
        return render_template('base.html')


APP.add_url_rule('/', view_func=IndexView.as_view('index'))


if __name__ == '__main__':
    APP.run(ENVIRONMENT_OBJECT.HOST)
