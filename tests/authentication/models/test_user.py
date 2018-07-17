from app.authentication.models import User, Role
from tests import BaseTestCase
from tests.authentication.helpers import create_role, delete_role

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

    def test_user_can_have_many_roles(self):
        self.user.create()

        self.assertEqual(len(self.user.roles), 0)

        role_1 = create_role(self.user.id)
        role_2 = create_role(self.user.id)

        self.assertEqual(len(self.user.roles), 2)

    def test_roles_can_be_deleted(self):
        self.user.create()
        role_1 = create_role(self.user.id)
        role_2 = create_role(self.user.id)
        self.assertEqual(len(self.user.roles), 2)

        delete_role(role_1.id)

        self.assertEqual(len(self.user.roles), 1)
