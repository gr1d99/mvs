from flask import url_for
from app.authentication.models import User
from tests import BaseTestCase


class LoginTestCase(BaseTestCase):
    def setUp(self):
        super(LoginTestCase, self).setUp()
        self.password = self.faker.password()
        self.email = self.faker.email()
        self.user = User(email=self.email, password=self.password)

    def test_user_can_login(self):
        self.user.create()

        response = self.client.post(
            url_for('authentication_app.login'),
            data=dict(
                email=self.user.email,
                password=self.password
            )
        )

        self.assert200(response)
        self.assertIn('auth_token', response.json)

    def test_cannot_login_with_wrong_credentials(self):
        response = self.client.post(
            url_for('authentication_app.login'),
            data=dict(
                email=self.faker.email(),
                password=self.faker.password
            )
        )

        self.assertStatus(response, 422)

    def test_failed_login_response_message(self):
        response = self.client.post(
            url_for('authentication_app.login'),
            data=dict(
                email=self.faker.email(),
                password=self.faker.password
            )
        )

        self.assertTrue(
            response.json['message'],
            'Invalid email or password'
        )
