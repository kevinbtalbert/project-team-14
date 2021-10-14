from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for


bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=('GET', 'POST'))
def products():
    """
    Route for the 'product' landing page
    """
    return render_template("products/products.html")