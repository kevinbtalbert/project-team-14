import os

from flask import Flask
from flaskext.mysql import MySQL


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True
    )
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        MYSQL_DATABASE_HOST='localhost',
        MYSQL_DATABASE_PORT='3306',
        MYSQL_DATABASE_USER='Team14',
        MYSQL_DATABASE_PASSWORD='password',
        MYSQL_DATABASE_DB=None,
        MYSQL_DATABASE_CHARSET='utf-8',

    )

    mysql = MySQL()
    mysql.init_app(app)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        cursor = mysql.get_db().cursor()
        print("hello world")
        print(cursor)
        return "Hello, World!"

    return app
