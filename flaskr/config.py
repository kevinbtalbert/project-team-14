import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    APP_NAME = os.getenv("APP_NAME", "flaskr")
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "b9d55c8721affe136a87dffcbb581")
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USE_TLS: True
    MAIL_USE_SSL: False
    MAIL_USERNAME: 'username@uncc.edu'
    MAIL_PASSWORD: 'mypassword'
    MAIL_DEFAULT_SERVER: 'mail.uncc.edu'
    MAIL_MAX_EMAILS: None
    MAIL_SUPPRESS_SEND: True


class DevelopmentConfig(BaseConfig):
    DATABASE = 'flaskr/database/appdata.db'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    DATABASE = 'flaskr/tests/test_database/test_appdata.db'
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True
    DATABASE_URI = 'mysql://Team14@localhost/users'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = 'Team14'
    MYSQL_DATABASE_PASSWORD = 'password'
    MYSQL_DATABASE_DB = 'users'
    MYSQL_DATABASE_CHARSET = None

class ProductionConfig(BaseConfig):
    PRODUCTION = True
    DEBUG = False
    DATABASE_URI = 'mysql://Team14@localhost/users'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = 'Team14'
    MYSQL_DATABASE_PASSWORD = 'password'
    MYSQL_DATABASE_DB = 'users'
    MYSQL_DATABASE_CHARSET = None
