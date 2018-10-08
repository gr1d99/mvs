import sqlalchemy
import uuid

from app.authentication.models import Blacklist
from tests import BaseTestCase


class BlacklistTestCase(BaseTestCase):
    def test_jti_cannot_be_empty(self):
        auth_token = None

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            Blacklist(jti=auth_token).create
        )

    def test_create_jti(self):
        jti = str(uuid.uuid1())
        Blacklist(jti=jti).create()

        self.assertIsNotNone(
            Blacklist.query.filter_by(jti=jti).first()
        )
