import sqlite3
import pandas as pd
from flask import Flask, current_app, g


def get_db():
    """
    Helper function to connect to the database 
    :return: database object
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    return db


def query_db(query, args=(), one=False):
    """
    Helper function to query the database based on arguments given at function call
    :param query: SQL statement to execute 
    :param args: parameters to use in SQL statement
    :param one: used in the case there are multiple returned object values, default value is False
    :return: database output from query
    """
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def update_db(query, args=(), one=False):
    """
    Helper function to update the databsae based on arguments given at function call
    :param query: SQL statement to execute 
    :param args: parameters to use in SQL statement
    :return: database response from commit
    """
    db = get_db()
    db.execute(query, args)
    res = db.commit()
    return res


def sql_to_df(sql, index=None):
    """
    Helper function to convert SQL query into DataFrame
    :param sql: string SQL query to run against database
    :param index: (optional) specify column index for DataFrame
    :return: dataframe of SQL query result
    """
    return pd.read_sql_query(sql, get_db(), index_col=index)


def close_db_connection(exception):
    """
    Helper function to close the connection to the database
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_app(app):
    """
    Initialize the app context and get the database object
    """
    with app.app_context():
        yield app


class DB_Commands:

    @staticmethod
    def find_all_profiles():
        """
        Find all customer profiles in database
        """
        return query_db("SELECT id, first_name, last_name, email, phone FROM profile", ())

    @staticmethod
    def find_profile_by_id(id):
        """
        Method to find a customer profile by its id
        """
        return query_db("SELECT id, first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state, address_zip, bust, waist, hip, chest, shoulders, inseam, neck, arm, anniversary FROM profile WHERE id = ?", (id,))


    @staticmethod
    def insert_new_profile(first_name="None Provided", last_name="None Provided", email="None Provided", phone="None Provided", dob="None Provided", gender="None Provided", address_street="None Provided", address_city="None Provided", address_state="None Provided", address_zip="None Provided"):
        """
        Command to insert a new profile based on passed in parameters
        """
        if first_name != "None Provided" and last_name != "None Provided":
            update_db("INSERT INTO profile (first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state, address_zip) VALUES (?,?,?,?,?,?,?,?,?,?)",
                      (first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state, address_zip,))
            try:
                profile_id = query_db("SELECT max(id) FROM profile", ())
                for idx in profile_id:
                    for idy in idx:
                        return idy
            except:
                return 0
        else:
            return 0


class Auth:

    @staticmethod
    def find_all_users():
        """
        Find all users in database and their associated data
        """
        return query_db("SELECT id, first_name, last_name, role, username FROM users", ())

    @staticmethod
    def find_user_id(username, password):
        """
        Find user id in database from username
        """
        try:
            user_id = query_db(
                "SELECT id FROM users WHERE username = ? AND password = ?", (username, password,))
            for value in user_id:
                user_id = value[0]
        except:
            user_id = 0
        return user_id

    @staticmethod
    def find_user_information(user_id):
        """
        Find user information from user's id
        """
        try:
            user_info = query_db(
                "SELECT id, first_name, last_name, role, username FROM users WHERE id = ?", (user_id,))
            for x in user_info:
                return [x[0], x[1], x[2], x[3], x[4]]
        except:
            return None
