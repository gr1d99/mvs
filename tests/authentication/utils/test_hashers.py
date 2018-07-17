import unittest

from faker import Faker

from app.authentication.utils import hashers


class HashersTestCase(unittest.TestCase):
    """hashers module test case"""

    def test_raw_password_is_hashed(self):
        raw_password = Faker().password()
        hashed_password = hashers.make_password(raw_password)

        self.assertNotEqual(raw_password, hashed_password)
