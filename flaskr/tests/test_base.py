from flask_testing import TestCase
from flaskr import create_app, db
from flask import current_app
from flaskr import config

app = create_app(config.TestingConfig)


class BaseTestCase(TestCase):

    def setUp(self):
        """
        Actions taken prior to running test cases
        """
        db.init_app(app)

    def tearDown(self):
        """
        Actions to take after finishing test cases
        """
        db.close_db_connection
