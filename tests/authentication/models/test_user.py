from app.authentication.models.user import User
from tests import BaseTestCase

import faker


FAKER = faker.Faker()


class UserTestCase(BaseTestCase):
    """User model TestCase"""

    def setUp(self):
        super(UserTestCase, self).setUp()
        self.raw_password = FAKER.password()
        self.user = User(email=FAKER.email(), password=self.raw_password)

    def test_user_is_created(self):
        self.assertEqual(User.query.count(), 0)
        self.user.create()
        self.assertEqual(User.query.first(), self.user)

    def test_user_is_deleted(self):
        self.assertEqual(User.query.count(), 0)
        self.user.create()
        self.user.delete()
        self.assertEqual(User.query.count(), 0)

    def test_password_is_hashed(self):
        self.user.create()
        self.assertNotEqual(self.user.password, self.raw_password)
