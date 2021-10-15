from flask_testing import TestCase

import flaskr.config
from flaskr import create_app, db
from flask import current_app
from flaskr import config

app = create_app()


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object(flaskr.config.BaseConfig)
        return app

    def setUp(self):
        """
        Actions taken prior to running test cases
        """
        pass

    def tearDown(self):
        """
        Actions to take after finishing test cases
        """
        pass

    def test_base_config(self):
        """
        Base Configuration Tests
        - Test that the base case debug flag is set to False
        - Test that base test testing flag is set to False
        """
        self.assertTrue(app.config["DEBUG"] is False)
        self.assertTrue(app.config["TESTING"] is False)

    # MYSQL DEPRECATED
    # def test_mysql_config(self):
    #     """
    #     Test MySQL Connection Settings
    #     """
    #     self.assertTrue(app.config["MYSQL_DATABASE_HOST"] is 'localhost')
    #     self.assertTrue(app.config["MYSQL_DATABASE_PORT"] == 3306)
    #     self.assertTrue(app.config["MYSQL_DATABASE_USER"] is 'Team14')
    #     self.assertTrue(app.config["MYSQL_DATABASE_PASSWORD"] is 'password')
    #     self.assertTrue(app.config["MYSQL_DATABASE_DB"] is 'users')
    #     self.assertTrue(app.config["MYSQL_DATABASE_CHARSET"] is None)
