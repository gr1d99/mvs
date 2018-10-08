from flask import jsonify
from flask.views import View

from flask_jwt_extended import (
    jwt_required, get_raw_jwt
)

from app.authentication.models import Blacklist
from app.authentication.utils import jwt


class LogoutView(View):
    """User logout handler"""

    decorators = [jwt_required, ]
    methods = ['DELETE', ]

    def dispatch_request(self):
        jti = get_raw_jwt()['jti']
        Blacklist(jti=jti).create()
        return jsonify(
            {'message': 'Successfully logged out'}
        ), 200
