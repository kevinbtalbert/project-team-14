import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    APP_NAME = os.getenv("APP_NAME", "flaskr")
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "b9d55c8721affe136a87dffcbb581")


class DevelopmentConfig(BaseConfig):
    SERVER_NAME = "localhost:8080"
    DATABASE = 'flaskr/database/appdata.db'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    DATABASE = 'flaskr/database/appdata.db'
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
