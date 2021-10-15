from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for


bp = Blueprint('marketing', __name__, url_prefix='/marketing')

@bp.route('/', methods=('GET', 'POST'))
def marketing():
    """
    Route for the 'product' landing page
    :return: rendered template
    """
    return render_template("marketing/email.html")