from flask_login import UserMixin
from . import db

class User(UserMixin):

    def __init__(self, usr_id):
        self.usr_id = usr_id
        user_info = db.Auth.find_user_information(usr_id)
        self.first_name = user_info[1]
        self.last_name = user_info[2]
        self.role = user_info[3]
        self.username = user_info[4]

    @property
    def id(self):
        return self.usr_id