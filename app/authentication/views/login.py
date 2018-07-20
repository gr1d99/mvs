from flask import jsonify, render_template
from flask.views import request, View
from flask_jwt_extended import create_access_token

from app.authentication.models import User


class LoginView(View):
    """User login view handler"""

    methods = ['GET', 'POST', ]

    def dispatch_request(self):
        if request.method == 'POST':
            error_message = dict(message='Invalid email or password')
            email = request.form.get('email', None)
            password = request.form.get('password', None)

            user = User.query.filter_by(email=email).first()

            if not user:
                return jsonify(error_message), 422

            if not user.check_password(password):
                return jsonify(error_message), 422

            token = create_access_token(identity=email)

            return jsonify(dict(auth_token=token)), 200

        else:
            return render_template('authentication/login.html', )
