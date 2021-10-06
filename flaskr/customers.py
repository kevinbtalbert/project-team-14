from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

@login_required
@bp.route('/customer/', methods=('GET', 'POST'))
def customer():
    """
    Route for the 'customer' landing page
    """
    return render_template("customer.html")