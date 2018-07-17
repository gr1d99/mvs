from flask_testing import TestCase
from app import APP, DB
from config import Testing


class BaseTestCase(TestCase):
    """Base TestCase for mvs application"""

    def create_app(self):
        APP.config.from_object(Testing)
        return APP

    def setUp(self):
        super(TestCase, self).setUp()
        DB.create_all()

    def tearDown(self):
        DB.session.remove()
        DB.drop_all()
