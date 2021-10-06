from wtforms import Form, StringField, SelectField, RadioField
from wtforms.validators import DataRequired, Required
from wtforms.widgets.core import Select

# This form captures all the customer profile's contact information
class ProfileContactForm(Form):
    first_name = StringField('', validators=[DataRequired()])
    pass

# This form captures all the customer profile's sizing information
class ProfileSizingForm(Form):
    pass

