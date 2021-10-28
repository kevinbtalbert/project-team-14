from wtforms import Form, StringField, SelectField, RadioField
from wtforms.validators import DataRequired, Required
from wtforms.widgets.core import Select

# This form captures all the customer profile's contact information
class ProfileContactForm(Form):
    STATES_LIST = ["", "AL", "AK", "AS", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
                   "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"]
    first_name = StringField('', validators=[DataRequired()])
    last_name = StringField('', validators=[DataRequired()])
    email = StringField('')
    phone = StringField('')
    dob = StringField('')
    gender = SelectField(
        '', choices=["", "Male", "Female", "Other Gender/Gender Nonconforming"])
    address_street = StringField('')
    address_city = StringField('')
    address_state = SelectField('', choices=STATES_LIST)
    address_zip = StringField('')

# This form captures the ability to lookup a customer profile by first and last name
class LookupCustomerForm(Form):
    first_name = StringField('', validators=[DataRequired()])
    last_name = StringField('', validators=[DataRequired()])


# This form captures the ability to lookup a customer by id
class SearchCustomerById(Form):
    id = StringField('', validators=[DataRequired()])


# This form captures all the customer profile's sizing information
class ProfileSizingForm(Form):
    bust = StringField('')
    waist = StringField('')
    hip = StringField('')
    chest = StringField('')
    shoulders = StringField('')
    inseam = StringField('')
    neck = StringField('')
    arm = StringField('')


# This form captures all the product information
class ProductForm(Form):
    CATEGORY_LIST = ["", "Outer wear", "Active wear", "Swimwear", "Tailored Clothing & Suits", "Social wear & Special occasions", "Casual & Sports wear", "Leg wear", "Neck wear",
                     "Shawls and wraps", "Bridal wear", "Evening wear", "Uniforms", "Knit wear", "Lounge wear", "Shirts and blouses", "Bottoms", "Sleep wear", "Other/Uncategorized"]
    DEPT_LIST = ["", "Mens", "Womens", "Unisex/NA"]
    product = StringField('', validators=[DataRequired()])
    product_image_url = StringField('')
    category = SelectField('', choices=CATEGORY_LIST)
    company = StringField('')
    company_logo_url = StringField('')
    department = SelectField('', choices=DEPT_LIST)
    msrp_cost = StringField('')
    wholesale_cost = StringField('')
    manufacturer = StringField('')
    inv_quantity = StringField('')
    description = StringField('')


# This form captures the ability to lookup a product by name
class LookupProductForm(Form):
    product = StringField('', validators=[DataRequired()])


# This form captures the ability to lookup a product by id
class SearchProductById(Form):
    id = StringField('', validators=[DataRequired()])


# This form captures the signin
class LoginForm(Form):
    username = StringField('', validators=[DataRequired()])
    password = StringField('', validators=[DataRequired()])
