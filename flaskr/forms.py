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
    gender = SelectField('', choices=["Male", "Female", "Other Gender/Gender Nonconforming"])
    address_street = StringField('')
    address_city = StringField('')
    address_state = SelectField('', choices=STATES_LIST)
    address_zip = StringField('')

# This form captures the ability to lookup a customer profile by first and last name
class LookupCustomerForm(Form):
    first_name = StringField('', validators=[DataRequired()])
    last_name = StringField('', validators=[DataRequired()])

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


# This form captures the signin
class LoginForm(Form):
    username = StringField('', validators=[DataRequired()])
    password = StringField('', validators=[DataRequired()])