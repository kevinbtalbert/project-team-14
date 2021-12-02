from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import Auth, DB_Commands, sql_to_df
from flaskr.forms import UserForm, ModifyUserForm, SearchUserById
bp = Blueprint('management', __name__, url_prefix='/management')

@bp.route('/', methods=('GET', 'POST'))
def management():
    """
    Route for the 'product' landing page
    :return: rendered template
    """
    headings = ("ID", "First Name", "Last Name", "Role", "Username", "Modify User")
    data = sql_to_df("SELECT id, first_name, last_name, role, username FROM users")
    data['Modify User'] = "Modify User"
    return render_template("management/management.html", headings=headings, data=data)


@bp.route('/new', methods=('GET', 'POST'))
def new_user():
    """
    Route for the 'new customer' landing page
    """
    new_user_form = UserForm(request.form)
    if request.method == 'POST':
        first_name = new_user_form.data['first_name']
        last_name = new_user_form.data['last_name']
        role = new_user_form.data['role']
        username = new_user_form.data['username']
        password = new_user_form.data['password']
        if new_user_form.data != None:
            Auth.insert_new_user(first_name.capitalize(), last_name.capitalize(), role, username, password)
        return redirect(url_for('management.management'))
    return render_template("management/new_user.html", form=new_user_form)


@bp.route('/lookup/<id>', methods=('GET', 'POST'))
def edit_user_by_id(id):
    """
    Route for editing customer profile by id
    :param id: represents the numerical id of the customer in the database
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
        role = edit_user_form.data['role']
        if role == "delete":
            Auth.delete_user(search_string)
            return redirect(url_for('management.management'))
        if role != "":
            Auth.update_user(search_string, role=role)
        first_name = edit_user_form.data['first_name']
        if first_name != "":
            Auth.update_user(search_string, first_name=first_name)
        last_name = edit_user_form.data['last_name']
        if last_name != "":
            Auth.update_user(search_string, last_name=last_name)
        username = edit_user_form.data['username']
        if username != "":
            Auth.update_user(search_string, username=username)

        return redirect(url_for('management.management'))

    profile_data = Auth.find_user_information(search_string)

    return render_template("management/edit_user.html", data=profile_data, form=edit_user_form)

