from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import DB_Commands, sql_to_df
from flaskr.forms import ProfileContactForm, ProfileSizingForm, LookupCustomerForm, SearchCustomerById
bp = Blueprint('customers', __name__, url_prefix='/customers')

@bp.route('/', methods=('GET', 'POST'))
def customers():
    """
    Route for the 'customer' landing page
    :return: rendered template
    """
    headings = ("Customer ID", "Customer First Name", "Customer Last Name", "Customer Email", "Customer Phone Number", "View Profile")
    df = sql_to_df("SELECT id, first_name, last_name, email, phone FROM profile")
    df["Profile"] = "View Profile"
    return render_template("customers/customers.html", headings=headings, data=df)


@bp.route('/new', methods=('GET', 'POST'))
def new_customer():
    """
    Route for the 'new customer' landing page
    """
    new_customer_form = ProfileContactForm(request.form)
    if request.method == 'POST':
        first_name = new_customer_form.data['first_name']
        last_name = new_customer_form.data['last_name']
        email = new_customer_form.data['email']
        phone = new_customer_form.data['phone']
        dob = new_customer_form.data['dob']
        gender = new_customer_form.data['gender']
        address_street = new_customer_form.data['address_street']
        address_city = new_customer_form.data['address_city']
        address_state = new_customer_form.data['address_state']
        address_zip = new_customer_form.data['address_zip']
        if new_customer_form.data != None:
            DB_Commands.insert_new_profile(first_name.capitalize(), last_name.capitalize(), email, phone, dob, gender, address_street, address_city, address_state, address_zip)
        return redirect(url_for('customers.customers'))
    return render_template("customers/new_customer.html", form=new_customer_form)


@bp.route('/lookup', methods=('GET', 'POST'))
def lookup_customer():
    """
    Route for the 'lookup customer' landing page
    :return: rendered template
    """
    lookup_customer_form = LookupCustomerForm(request.form)
    if request.method == 'POST':
        first_name = lookup_customer_form.data['first_name']
        last_name = lookup_customer_form.data['last_name']
        try:
            id = DB_Commands.find_profile_id_by_name(first_name.capitalize(), last_name.capitalize())
            for value in id:
                id_to_search = value[0]
            return redirect(url_for('customers.customer_profile_by_id', id=id_to_search))
        except:
            flash("Profile not found")
    return render_template("customers/lookup_customer.html", form=lookup_customer_form)


@bp.route('/lookup/<id>', methods=('GET', 'POST'))
def customer_profile_by_id(id=None):
    """
    Route for looking up customer by id
    :param id: represents the numerical id of the customer in the database (assumes None by default)
    :return: rendered template
    """
    try:
        search_string = id.data['search']
    except:
        search_string = str(id)
        id = SearchCustomerById(request.form)
        id.data['search'] = search_string

    profile_data = DB_Commands.find_profile_by_id(search_string)
    for data in profile_data:
        profile=data

    return render_template("customers/profile_customer.html", data=profile)


@bp.route('/lookup/<id>/edit_profile', methods=('GET', 'POST'))
def edit_customer_profile_by_id(id):
    """
    Route for editing customer profile by id
    :param id: represents the numerical id of the customer in the database
    :return: rendered template
    """
    edit_customer_form = ProfileContactForm(request.form)
    try:
        search_string = id.data['search']
    except:
        search_string = str(id)
        id = SearchCustomerById(request.form)
        id.data['search'] = search_string
    
    if request.method == "POST":
        email = edit_customer_form.data['email']
        if email != "":
            DB_Commands.update_profile(search_string, email=email)
        phone = edit_customer_form.data['phone']
        if phone != "":
            DB_Commands.update_profile(search_string, phone=phone)
        dob = edit_customer_form.data['dob']
        if dob != "":
            DB_Commands.update_profile(search_string, dob=dob)
        gender = edit_customer_form.data['gender']
        if gender != "":
            DB_Commands.update_profile(search_string, gender=gender)
        address_street = edit_customer_form.data['address_street']
        if address_street != "":
            DB_Commands.update_profile(search_string, address_street=address_street)
        address_city = edit_customer_form.data['address_city']
        if address_city != "":
            DB_Commands.update_profile(search_string, address_city=address_city)
        address_state = edit_customer_form.data['address_state']
        if address_state != "":
            DB_Commands.update_profile(search_string, address_state=address_state)
        address_zip = edit_customer_form.data['address_zip']
        if address_zip != "":
            DB_Commands.update_profile(search_string, address_zip=address_zip)

        return redirect(url_for('customers.customer_profile_by_id', id=search_string))

    profile_data = DB_Commands.find_profile_by_id(search_string)
    for data in profile_data:
        profile=data

    return render_template("customers/edit_profile_customer.html", data=profile, form=edit_customer_form)


@bp.route('/lookup/<id>/edit_sizing', methods=('GET', 'POST'))
def edit_customer_sizing_by_id(id):
    """
    Route for editing customer sizing by id
    :param id: represents the numerical id of the customer in the database
    :return: rendered template
    """
    edit_customer_form = ProfileSizingForm(request.form)
    try:
        search_string = id.data['search']
    except:
        search_string = str(id)
        id = SearchCustomerById(request.form)
        id.data['search'] = search_string
    
    if request.method == "POST":
        bust = edit_customer_form.data['bust']
        if bust != "":
            DB_Commands.update_profile(search_string, bust=bust)
        waist = edit_customer_form.data['waist']
        if waist != "":
            DB_Commands.update_profile(search_string, waist=waist)
        hip = edit_customer_form.data['hip']
        if hip != "":
            DB_Commands.update_profile(search_string, hip=hip)
        chest = edit_customer_form.data['chest']
        if chest != "":
            DB_Commands.update_profile(search_string, chest=chest)
        shoulders = edit_customer_form.data['shoulders']
        if shoulders != "":
            DB_Commands.update_profile(search_string, shoulders=shoulders)
        inseam = edit_customer_form.data['inseam']
        if inseam != "":
            DB_Commands.update_profile(search_string, inseam=inseam)
        neck = edit_customer_form.data['neck']
        if neck != "":
            DB_Commands.update_profile(search_string, neck=neck)
        arm = edit_customer_form.data['arm']
        if arm != "":
            DB_Commands.update_profile(search_string, arm=arm)

        return redirect(url_for('customers.customer_profile_by_id', id=search_string))

    profile_data = DB_Commands.find_profile_by_id(search_string)
    for data in profile_data:
        profile=data

    return render_template("customers/edit_sizing_customer.html", data=profile, form=edit_customer_form)


@bp.route('/lookup/<id>/delete_profile', methods=('GET', 'POST'))
def delete_customer_by_id(id):
    """
    Route for deleting customer profile by id
    :param id: represents the numerical id of the customer in the database
    :return: rendered template
    """
    edit_customer_form = ProfileContactForm(request.form)
    try:
        search_string = id.data['search']
    except:
        search_string = str(id)
        id = SearchCustomerById(request.form)
        id.data['search'] = search_string
    
    profile_data = DB_Commands.find_profile_by_id(search_string)
    for data in profile_data:
        profile=data

    if request.method == "POST":
        DB_Commands.delete_profile(search_string)
        return redirect(url_for('customers.customers'))

    return render_template("customers/delete_profile_customer.html", data=profile, form=edit_customer_form)