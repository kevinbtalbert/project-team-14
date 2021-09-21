import os

from flask import Flask
from flaskext.mysql import MySQL


def create_app(config=None):
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        instance_relative_config=True
    )

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_object(config)

    mysql = MySQL()
    mysql.init_app(app)

    def query_db(sql):
        """
        Helper function to query the database
        :return: database object
        """
        cursor = mysql.get_db().cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    @app.route("/hello")
    def hello():
        print(query_db("SELECT * FROM users"))
        print("hello world")
        return "Hello, World!"

    return app
