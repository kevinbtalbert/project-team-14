import os
import logging
from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, login_manager, login_required, logout_user, login_user, current_user
from flaskr.models import User
from flaskr.db import Auth, DB_Commands
from flaskr.forms import LoginForm, ModifyUserForm, SearchUserById
from flaskext.mysql import MySQL
import pandas as pd
from flask_mail import Mail, Message

mail = Mail()

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

    logging.basicConfig(filename='btms_logging.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    mail.init_app(app)
    mail.app = app

    mysql = MySQL()
    mysql.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @app.route("/")
    @app.route("/index")
    def home():
        return render_template("index.html")

    @app.route("/login",  methods=('GET', 'POST'))
    def login():
        login_form = LoginForm(request.form)
        if request.method == 'POST':
            try:
                username = login_form.data['username']
                password = login_form.data['password']
                user_id = Auth.find_user_id(username, password)
                if user_id > 0:
                    user = load_user(user_id)
                    login_user(user)
                    return redirect('/')
                else:
                    return redirect('/login')
            except:
                print("Exception occured")
        return render_template("utils/signin.html", form=login_form)

    @login_manager.user_loader
    def load_user(id):
        """
        Required module by the login manager for loading the user
        """
        return User(id)

    @app.route('/logout')
    @login_required
    def logout():
        """
        Logout handler which removes current user from session
        """
        logout_user()
        return redirect('/index')

    @app.route('/my_profile')
    @login_required
    def my_profile():
        """
        Profile viewer which shows individual's profile who is logged into the app
        """
        return render_template("utils/my_profile.html")

    @app.route('/my_profile/<id>', methods=('GET', 'POST'))
    def edit_my_profile_by_id(id):
        """
        Route for editing user's profile by id
        :param id: represents the numerical id of the user in the database
        :return: rendered template
        """
        edit_user_form = ModifyUserForm(request.form)
        try:
            search_string = id.data['search']
        except:
            search_string = str(id)
            id = SearchUserById(request.form)
            id.data['search'] = search_string
        
        if request.method == "POST":
            username = edit_user_form.data['username']
            if username != "":
                Auth.update_user(search_string, username=username)
            password = edit_user_form.data['password']
            if password != "":
                Auth.update_user(search_string, password=password)
            return redirect(url_for('my_profile'))

        profile_data = Auth.find_user_information(search_string)
        return render_template("utils/edit_my_profile.html", data=profile_data, form=edit_user_form)
    
    @app.errorhandler(404)
    def page_not_found(e):
        """
        Set the 404 error route handler explicitly
        """
        return render_template('utils/404.html')

    from . import customers, products, management, marketing
    app.register_blueprint(customers.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(management.bp)
    app.register_blueprint(marketing.bp)

    return app
