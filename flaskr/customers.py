from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import DB_Commands, sql_to_df
from flaskr.forms import ProfileContactForm, LookupCustomerForm, SearchCustomerById
bp = Blueprint('customers', __name__, url_prefix='/customers')

@bp.route('/', methods=('GET', 'POST'))
def customers():
    """
    Route for the 'customer' landing page
    """
    headings = ("Customer ID", "Customer First Name", "Customer Last Name", "Customer Email", "Customer Phone Number", "View Profile")
    df = sql_to_df("SELECT id, first_name, last_name, email, phone FROM profile")
    df["Profile"] = "View Profile"
    print(df)
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
            DB_Commands.insert_new_profile(first_name, last_name, email, phone, dob, gender, address_street, address_city, address_state, address_zip)
    return render_template("customers/new_customer.html", form=new_customer_form)


@bp.route('/lookup', methods=('GET', 'POST'))
def lookup_customer():
    """
    Route for the 'lookup customer' landing page
    """
    lookup_customer_form = LookupCustomerForm(request.form)
    if request.method == 'POST':
        print (lookup_customer_form.data)
    return render_template("customers/lookup_customer.html", form=lookup_customer_form)


@bp.route('/lookup/<id>', methods=('GET', 'POST'))
def customer_profile_by_id(id):
    """
    Route for looking up customer by id
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