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
        MYSQL_DATABASE_PORT=3306,
        MYSQL_DATABASE_USER='Team14',
        MYSQL_DATABASE_PASSWORD='password',
        MYSQL_DATABASE_DB='users',
        MYSQL_DATABASE_CHARSET=None,
    )

    mysql = MySQL()
    mysql.init_app(app)

    @app.route("/hello")
    def hello():
        cursor = mysql.get_db().cursor()
        cursor.execute("USE users")
        user = cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
        print(rows)
        print("hello world")
        return "Hello, World!"

    return app
