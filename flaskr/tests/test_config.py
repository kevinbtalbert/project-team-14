from flask import current_app
from flaskr import create_app
from flask_testing import TestCase

app = create_app()


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        """
        Create app from DEVELOPMENT configuration in config.py for testing
        """
        app.config.from_object("flaskr.config.DevelopmentConfig")
        return app

    def test_app_is_development(self):
        """
        Development Configuration Tests
        - Test that the current app is not in TESTING configuration
        - Test that the app is running the DEVELOPMENT configuration
        - Test that the debugging configurations are enabled
        """
        self.assertFalse(current_app.config["TESTING"])
        self.assertTrue(app.config["DEVELOPMENT"] is True)
        self.assertTrue(app.config["DEBUG"] is True)


class TestTestingConfig(TestCase):

    def create_app(self):
        """
        Create app from TESTING configuration in config.py for testing
        """
        app.config.from_object("flaskr.config.TestingConfig")
        return app

    def test_app_is_testing(self):
        """
        Testing Configuration Tests
        - Test that the current app is in TESTING configuration
        - Test that the preserve context on exception flag is disabled
        - Test that the debugging configurations are enabled
        - Test that the app is running the TESTING configuration
        """
        self.assertTrue(current_app.config["TESTING"])
        self.assertTrue(app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] is False)
        self.assertTrue(app.config["DEBUG"] is True)
        self.assertTrue(app.config["TESTING"] is True)


class TestStagingConfig(TestCase):

    def create_app(self):
        """
        Create app from STAGING configuration in config.py for testing
        """
        app.config.from_object("flaskr.config.StagingConfig")
        return app

    def test_app_is_staging(self):
        """
        Staging Configuration Tests
        - Test that the current app is not in TESTING configuration
        - Test that the app is running the DEVELOPMENT configuration
        - Test that the debugging configurations are enabled
        """
        self.assertFalse(current_app.config["TESTING"])
        self.assertTrue(app.config["DEVELOPMENT"] is True)
        self.assertTrue(app.config["DEBUG"] is True)


class TestProductionConfig(TestCase):

    def create_app(self):
        """
        Create app from PRODUCTION configuration in config.py for testing
        """
        app.config.from_object("flaskr.config.ProductionConfig")
        return app

    def test_app_is_production(self):
        """
        Production Configuration Tests
        - Test that the current app is not in TESTING configuration
        - Test that the app is running the PRODUCTION configuration
        - Test that the debugging configurations are disabled
        """
        self.assertFalse(current_app.config["TESTING"])
        self.assertTrue(app.config["PRODUCTION"] is True)
        self.assertTrue(app.config["DEBUG"] is False)
