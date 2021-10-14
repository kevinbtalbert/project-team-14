from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import DB_Commands
bp = Blueprint('management', __name__, url_prefix='/management')

@bp.route('/', methods=('GET', 'POST'))
def management():
    """
    Route for the 'product' landing page
    """
    return render_template("management/management.html")


@bp.route('/users/', methods=('GET', 'POST'))
def users():
    """
    Route for the 'product' landing page
    """
    data = DB_Commands.find_all_users()
    return render_template("management/users.html", data=data)


def lookup_user(user):
    pass
