"""User authentication application"""

from flask import Blueprint
from .views import LoginView

AUTHENTICATION_APP = Blueprint(
    'authentication_app',
    __name__,
    template_folder='templates'
)

AUTHENTICATION_APP.add_url_rule('/login', view_func=LoginView.as_view('login'))
