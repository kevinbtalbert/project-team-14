from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

@bp.route('/', methods=('GET', 'POST'))
def product():
    """
    Route for the 'product' landing page
    """
    return render_template("product.html")