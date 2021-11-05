import sqlite3
import pandas as pd
from flask import Flask, current_app, g
from fuzzywuzzy import fuzz


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
        :param id: integer value of id in the database
        :return: result of query to database
        """
        return query_db("SELECT id, first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state, address_zip, bust, waist, hip, chest, shoulders, inseam, neck, arm, anniversary FROM profile WHERE id = ?", (id,))


    @staticmethod
    def find_profile_id_by_name(first_name, last_name):
        """
        Method to find a customer profile id by first and last name
        :param first_name: string value of first_name in the database
        :param last_name: string value of first_name in the database
        :return: result of query to database
        """
        return query_db("SELECT id FROM profile WHERE first_name = ? AND last_name = ?", (first_name, last_name,))


    @staticmethod
    def insert_new_profile(first_name="None Provided", last_name="None Provided", email="None Provided", phone="None Provided", dob="None Provided", gender="None Provided", address_street="None Provided", address_city="None Provided", address_state="None Provided", address_zip="None Provided"):
        """
        Command to insert a new profile based on passed in parameters
        :param first_name: string value of first_name in the database (if not supplied, parameter assumes "None Provided")
        :param last_name: string value of last_name in the database (if not supplied, parameter assumes "None Provided")
        :param email: string value of email in the database (if not supplied, parameter assumes "None Provided")
        :param phone: string value of phone in the database (if not supplied, parameter assumes "None Provided")
        :param dob: string value of dob in the database (if not supplied, parameter assumes "None Provided")
        :param gender: string value of gender in the database (if not supplied, parameter assumes "None Provided")
        :param address_street: string value of address_street in the database (if not supplied, parameter assumes "None Provided")
        :param address_city: string value of address_city in the database (if not supplied, parameter assumes "None Provided")
        :param address_state: string value of address_state in the database (if not supplied, parameter assumes "None Provided")
        :param address_zip: string value of address_zip in the database (if not supplied, parameter assumes "None Provided")
        :return: integer value of id, the newest profile in the database
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


    @staticmethod
    def update_profile(id, first_name=None, last_name=None, email=None, phone=None, dob=None, gender=None, address_street=None, address_city=None, address_state=None, address_zip=None, bust=None, waist=None, hip=None, chest=None, shoulders=None, inseam=None, neck=None, arm=None):
        """
        Command to update particular elements of a customer's profile
        :param first_name: string value of first_name in the database (if not supplied, parameter assumes "None Provided")
        :param last_name: string value of last_name in the database (if not supplied, parameter assumes "None Provided")
        :param email: string value of email in the database (if not supplied, parameter assumes "None Provided")
        :param phone: string value of phone in the database (if not supplied, parameter assumes "None Provided")
        :param dob: string value of dob in the database (if not supplied, parameter assumes "None Provided")
        :param gender: string value of gender in the database (if not supplied, parameter assumes "None Provided")
        :param address_street: string value of address_street in the database (if not supplied, parameter assumes "None Provided")
        :param address_city: string value of address_city in the database (if not supplied, parameter assumes "None Provided")
        :param address_state: string value of address_state in the database (if not supplied, parameter assumes "None Provided")
        :param address_zip: string value of address_zip in the database (if not supplied, parameter assumes "None Provided")
        :param bust: string value of bust in the database (if not supplied, parameter assumes "None Provided")
        :param waist: string value of waist in the database (if not supplied, parameter assumes "None Provided")
        :param hip: string value of hip in the database (if not supplied, parameter assumes "None Provided")
        :param chest: string value of chest in the database (if not supplied, parameter assumes "None Provided")
        :param shoulders: string value of shoulders in the database (if not supplied, parameter assumes "None Provided")
        :param inseam: string value of inseam in the database (if not supplied, parameter assumes "None Provided")
        :param neck: string value of neck in the database (if not supplied, parameter assumes "None Provided")
        :param arm: string value of arm in the database (if not supplied, parameter assumes "None Provided")
        """
        args = locals()
        for param, value in args.items():
            if value is not None:
                if param == "email":
                    update_db(
                        "UPDATE profile SET email=? WHERE id=?", (value, id,))
                if param == "phone":
                    update_db(
                        "UPDATE profile SET phone=? WHERE id=?", (value, id,))
                if param == "dob":
                    update_db(
                        "UPDATE profile SET dob=? WHERE id=?", (value, id,))
                if param == "gender":
                    update_db(
                        "UPDATE profile SET gender=? WHERE id=?", (value, id,))
                if param == "address_street":
                    update_db(
                        "UPDATE profile SET address_street=? WHERE id=?", (value, id,))
                if param == "address_city":
                    update_db(
                        "UPDATE profile SET address_city=? WHERE id=?", (value, id,))
                if param == "address_state":
                    update_db(
                        "UPDATE profile SET address_state=? WHERE id=?", (value, id,))
                if param == "address_zip":
                    update_db(
                        "UPDATE profile SET address_zip=? WHERE id=?", (value, id,))
                if param == "bust":
                    update_db(
                        "UPDATE profile SET bust=? WHERE id=?", (value, id,))
                if param == "waist":
                    update_db(
                        "UPDATE profile SET waist=? WHERE id=?", (value, id,))
                if param == "hip":
                    update_db(
                        "UPDATE profile SET hip=? WHERE id=?", (value, id,))
                if param == "chest":
                    update_db(
                        "UPDATE profile SET chest=? WHERE id=?", (value, id,))
                if param == "shoulders":
                    update_db(
                        "UPDATE profile SET shoulders=? WHERE id=?", (value, id,))
                if param == "inseam":
                    update_db(
                        "UPDATE profile SET inseam=? WHERE id=?", (value, id,))
                if param == "neck":
                    update_db(
                        "UPDATE profile SET neck=? WHERE id=?", (value, id,))
                if param == "arm":
                    update_db(
                        "UPDATE profile SET arm=? WHERE id=?", (value, id,))


    @staticmethod
    def delete_profile(id):
        """
        Command to delete customer's profile by id
        :param id: integer value of id, the newest profile in the database
        """
        update_db("DELETE FROM profile WHERE id=?", (id,))


    @staticmethod
    def find_all_products():
        """
        Find all products summary information in database
        """
        return query_db("SELECT id, product, category, company, department, msrp_cost FROM products", ())
    

    @staticmethod
    def find_product_by_id(id):
        """
        Method to find a product's information by its id
        :param id: integer value of id in the database
        :return: result of query to database
        """
        return query_db("SELECT id, product, product_image_url, category, company, company_logo_url, department, msrp_cost, wholesale_cost, manufacturer, inv_quantity, description, last_updated FROM products WHERE id = ?", (id,))


    @staticmethod
    def find_product_id_by_name(product_name):
        """
        Method to find a product id by product name
        Uses fuzzywuzzy module to locate highest likelihood product in database
        :param product_name: string value of product in the database
        :return: result of query to database
        """
        existing_products = query_db("SELECT product FROM products", ())
        product_proximity = 0
        for product in existing_products:
            for value in product:
                if fuzz.ratio(value, product_name) > product_proximity:
                    product_proximity = fuzz.ratio(value, product_name)
                    product_name = value
        return query_db("SELECT id FROM products WHERE product = ?", (product_name,))

    
    @staticmethod
    def insert_new_product(product="None Provided", product_image_url="None Provided", category="None Provided", company="None Provided", company_logo_url="None Provided", department="None Provided", msrp_cost="None Provided", wholesale_cost="None Provided", manufacturer="None Provided", inv_quantity="None Provided", description="None Provided"):
        """
        Command to insert a new profile based on passed in parameters
        :param product: string value of product in the database (if not supplied, parameter assumes "None Provided")
        :param product_image_url: string value of product_image_url in the database (if not supplied, parameter assumes "None Provided")
        :param category: string value of category in the database (if not supplied, parameter assumes "None Provided")
        :param company: string value of company in the database (if not supplied, parameter assumes "None Provided")
        :param company_logo_url: string value of company_logo_url in the database (if not supplied, parameter assumes "None Provided")
        :param department: string value of department in the database (if not supplied, parameter assumes "None Provided")
        :param msrp_cost: string value of msrp_cost in the database (if not supplied, parameter assumes "None Provided")
        :param wholesale_cost: string value of wholesale_cost in the database (if not supplied, parameter assumes "None Provided")
        :param manufacturer: string value of manufacturer in the database (if not supplied, parameter assumes "None Provided")
        :param inv_quantity: string value of inv_quantity in the database (if not supplied, parameter assumes "None Provided")
        :param description: string value of inv_quantity in the database (if not supplied, parameter assumes "None Provided")
        :return: integer value of id, the newest profile in the database
        """
        if product != "None Provided":
            update_db("INSERT INTO products (product, product_image_url, category, company, company_logo_url, department, msrp_cost, wholesale_cost, manufacturer, inv_quantity, description) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                      (product, product_image_url, category, company, company_logo_url, department, msrp_cost, wholesale_cost, manufacturer, inv_quantity, description,))
            try:
                profile_id = query_db("SELECT max(id) FROM profile", ())
                for idx in profile_id:
                    for idy in idx:
                        return idy
            except:
                return 0
        else:
            return 0


    @staticmethod
    def update_product(id, product=None, product_image_url=None, category=None, company=None, company_logo_url=None, department=None, msrp_cost=None, wholesale_cost=None, manufacturer=None, inv_quantity=None, description=None):
        """
        Command to update particular elements of a customer's profile
        :param product: string value of product in the database (if not supplied, parameter assumes "None Provided")
        :param product_image_url: string value of product_image_url in the database (if not supplied, parameter assumes "None Provided")
        :param category: string value of category in the database (if not supplied, parameter assumes "None Provided")
        :param company: string value of company in the database (if not supplied, parameter assumes "None Provided")
        :param company_logo_url: string value of company_logo_url in the database (if not supplied, parameter assumes "None Provided")
        :param department: string value of department in the database (if not supplied, parameter assumes "None Provided")
        :param msrp_cost: string value of msrp_cost in the database (if not supplied, parameter assumes "None Provided")
        :param wholesale_cost: string value of wholesale_cost in the database (if not supplied, parameter assumes "None Provided")
        :param manufacturer: string value of manufacturer in the database (if not supplied, parameter assumes "None Provided")
        :param inv_quantity: string value of inv_quantity in the database (if not supplied, parameter assumes "None Provided")
        :param description: string value of description in the database (if not supplied, parameter assumes "None Provided")
        """
        args = locals()
        for param, value in args.items():
            if value is not None:
                if param == "product_image_url":
                    update_db(
                        "UPDATE products SET product_image_url=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "category":
                    update_db(
                        "UPDATE products SET category=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "company":
                    update_db(
                        "UPDATE products SET company=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "company_logo_url":
                    update_db(
                        "UPDATE products SET company_logo_url=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "department":
                    update_db(
                        "UPDATE products SET department=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "msrp_cost":
                    update_db(
                        "UPDATE products SET msrp_cost=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "wholesale_cost":
                    update_db(
                        "UPDATE products SET wholesale_cost=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "manufacturer":
                    update_db(
                        "UPDATE products SET manufacturer=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "inv_quantity":
                    update_db(
                        "UPDATE products SET inv_quantity=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                if param == "description":
                    update_db(
                        "UPDATE products SET description=?, last_updated=CURRENT_TIMESTAMP WHERE id=?", (value, id,))
                
    
    @staticmethod
    def delete_product(id):
        """
        Command to delete product by id
        :param id: integer value of id
        """
        update_db("DELETE FROM products WHERE id=?", (id,))


    @staticmethod
    def search_module(product_name):
        """
        Method to find a product id by product name
        Uses fuzzywuzzy module to locate highest likelihood product in database
        :param search_string: string value of what is to be searched in the database
        :return: result of query to database
        """
        existing_products = query_db("SELECT product FROM products", ())
        product_proximity = 0
        for product in existing_products:
            for value in product:
                if fuzz.ratio(value, product_name) > product_proximity:
                    product_proximity = fuzz.ratio(value, product_name)
                    product_name = value
        return query_db("SELECT id FROM products WHERE product = ?", (product_name,))

class Auth:

    @staticmethod
    def find_all_users():
        """
        Find all users in database and their associated data
        :return result of query to database for all users
        """
        return query_db("SELECT id, first_name, last_name, role, username FROM users", ())


    @staticmethod
    def find_user_id(username, password):
        """
        Find user id in database from username
        :param username: string username of the user
        :param password: string password of the user
        :return: user id if successful, 0 if not found
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
        :return: dictionary list of user information
        """
        try:
            user_info = query_db(
                "SELECT id, first_name, last_name, role, username FROM users WHERE id = ?", (user_id,))
            for x in user_info:
                return [x[0], x[1], x[2], x[3], x[4]]
        except:
            return None
