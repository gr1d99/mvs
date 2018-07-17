import sqlalchemy
from app.authentication.models.role import Role
from tests import BaseTestCase


class RoleTestCase(BaseTestCase):
    def setUp(self):
        super(RoleTestCase, self).setUp()
        self.role = Role(name='admin', description=self.faker.text())

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
