"""
    Test cases for login view
"""

from app.authentication.models import User
from tests import BaseTestCase
from tests.authentication.helpers import login_user


class LoginTestCase(BaseTestCase):
    def setUp(self):
        super(LoginTestCase, self).setUp()
        self.password = self.faker.password()
        self.email = self.faker.email()
        self.user = User(email=self.email, password=self.password)

    def test_user_can_login(self):
        self.user.create()

        response = login_user(self.client, self.user.email, self.password)

        self.assert200(response)
        self.assertIn('auth_token', response.json)

    def test_cannot_login_with_wrong_credentials(self):
        response = login_user(self.client, self.faker.email(), self.faker.password())
        self.assertStatus(response, 422)

    def test_failed_login_response_message(self):
        response = login_user(self.client, self.faker.email(), self.faker.password())
        self.assertTrue(
            response.json['message'],
            'Invalid email or password'
        )
