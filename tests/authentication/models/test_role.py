import sqlalchemy
from app.authentication.models import Role, User
from tests import BaseTestCase


class RoleTestCase(BaseTestCase):
    def setUp(self):
        super(RoleTestCase, self).setUp()
        user = User(email=self.faker.email(), password=self.faker.password())
        user.create()
        self.role = Role(name='admin', description=self.faker.text(), user_id=user.id)

    def test_role_is_created(self):
        self.role.create()
        self.assertGreater(Role.query.count(), 0)
        self.assertEqual(self.role, Role.query.first())

    def test_role_is_deleted(self):
        self.assertEqual(Role.query.count(), 0)
        self.role.create()
        self.role.delete()
        self.assertEqual(Role.query.count(), 0)

    def test_role_name_cannot_be_null(self):
        self.role.name = None
        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.role.create
        )

    def test_role_user_cannot_be_null(self):
        self.role.user_id = None
        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.role.create
        )

    def test_user_is_associated_to_a_role(self):
        self.role.create()
        self.assertIs(User.query.first(), self.role.user)
