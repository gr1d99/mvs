import time

from datetime import timedelta

from app.authentication.models import User
from tests import BaseTestCase
from tests.authentication.helpers import (
    login_user, logout_user, user_token
)


class LogoutTestCase(BaseTestCase):
    def setUp(self):
        super(LogoutTestCase, self).setUp()
        self.email = self.faker.email()
        self.password = self.faker.password()
        self.user = User(email=self.email, password=self.password)
        self.user.create()
        response = login_user(self.client, self.email, self.password)
        self.auth_token = user_token(response)

    def test_successful_logout(self):
        response = logout_user(self.client, self.auth_token)

        self.assert200(response)
        self.assertTrue(response.json['message'], 'Successfully logged out')

    def test_token_cannot_be_used_twice_to_logout(self):
        logout_user(self.client, self.auth_token)
        response = logout_user(self.client, self.auth_token)

        self.assert401(response)
        self.assertTrue(response.json['message'], 'Token has been revoked')

    def test_expired_token(self):
        self.app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=1)
        logout_user(self.client, self.auth_token)
        time.sleep(1.1)
        response = logout_user(self.client, self.auth_token)

        self.assert401(response)
        self.assertTrue(response.json['message'], 'Token has expired')
