from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import DB_Commands, sql_to_df
from flaskr.forms import ProductForm, LookupProductForm, SearchProductById
bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=('GET', 'POST'))
def products():
    """
    Route for the 'products' landing page
    :return: rendered template
    """
    headings = ("Product ID", "Product Name", "Category", "Company", "Department", "MSRP", "View Product")
    df = sql_to_df("SELECT id, product, category, company, department, msrp_cost FROM products")
    df["Product"] = "View Product"
    return render_template("products/products.html", headings=headings, data=df)


@bp.route('/new', methods=('GET', 'POST'))
def new_product():
    """
    Route for the 'new product' landing page
    """
    new_product_form = ProductForm(request.form)
    if request.method == 'POST':
        product = new_product_form.data['product']
        product_image_url = new_product_form.data['product_image_url']
        category = new_product_form.data['category']
        company = new_product_form.data['company']
        company_logo_url = new_product_form.data['company_logo_url']
        department = new_product_form.data['department']
        msrp_cost = new_product_form.data['msrp_cost']
        wholesale_cost = new_product_form.data['wholesale_cost']
        manufacturer = new_product_form.data['manufacturer']
        inv_quantity = new_product_form.data['inv_quantity']
        description = new_product_form.data['description']
        if new_product_form.data != None:
            DB_Commands.insert_new_product(product.capitalize(), product_image_url, category, company, company_logo_url, department, msrp_cost, wholesale_cost, manufacturer, inv_quantity, description)
        return redirect(url_for('products.products'))
    return render_template("products/new_product.html", form=new_product_form)


@bp.route('/lookup', methods=('GET', 'POST'))
def lookup_product():
    """
    Route for the 'lookup product' landing page
    :return: rendered template
    """
    lookup_product_form = LookupProductForm(request.form)
    
    if request.method == 'POST':
        product_name = lookup_product_form.data['product']
        try:
            id = DB_Commands.find_product_id_by_name(product_name.capitalize())
            for value in id:
                id_to_search = value[0]
            return redirect(url_for('products.product_by_id', id=id_to_search))
        except:
            flash("Profile not found")
    return render_template("products/lookup_product.html", form=lookup_product_form)


@bp.route('/lookup/<id>', methods=('GET', 'POST'))
def product_by_id(id=None):
    """
    Route for looking up a product by id
    :param id: represents the numerical id of the product in the database (assumes None by default)
    :return: rendered template
    """
    try:
        search_string = id.data['search']
    except:
        search_string = str(id)
        id = SearchProductById(request.form)
        id.data['search'] = search_string

    profile_data = DB_Commands.find_product_by_id(search_string)
    for data in profile_data:
        profile=data

    return render_template("products/profile_product.html", data=profile)


@bp.route('/lookup/<id>/edit_product', methods=('GET', 'POST'))
def edit_product_by_id(id):
    """
    Route for editing product by id
    :param id: represents the numerical id of the product in the database
    :return: rendered template
    """
    edit_product_form = ProductForm(request.form)
    try:
        search_string = id.data['search']
    except:
        search_string = str(id)
        id = SearchProductById(request.form)
        id.data['search'] = search_string
    
    if request.method == "POST":
        product = edit_product_form.data['product']
        if product != "":
            DB_Commands.update_product(search_string, product=product)
        product_image_url = edit_product_form.data['product_image_url']
        if product_image_url != "":
            DB_Commands.update_product(search_string, product_image_url=product_image_url)
        category = edit_product_form.data['category']
        if category != "":
            DB_Commands.update_product(search_string, category=category)
        company = edit_product_form.data['company']
        if company != "":
            DB_Commands.update_product(search_string, company=company)
        company_logo_url = edit_product_form.data['company_logo_url']
        if company_logo_url != "":
            DB_Commands.update_product(search_string, company_logo_url=company_logo_url)
        department = edit_product_form.data['department']
        if department != "":
            DB_Commands.update_product(search_string, department=department)
        msrp_cost = edit_product_form.data['msrp_cost']
        if msrp_cost != "":
            DB_Commands.update_product(search_string, msrp_cost=msrp_cost)
        wholesale_cost = edit_product_form.data['wholesale_cost']
        if wholesale_cost != "":
            DB_Commands.update_product(search_string, wholesale_cost=wholesale_cost)
        manufacturer = edit_product_form.data['manufacturer']
        if manufacturer != "":
            DB_Commands.update_product(search_string, manufacturer=manufacturer)
        inv_quantity = edit_product_form.data['inv_quantity']
        if inv_quantity != "":
            DB_Commands.update_product(search_string, inv_quantity=inv_quantity)
        description = edit_product_form.data['description']
        if description != "":
            DB_Commands.update_product(search_string, description=description)

        return redirect(url_for('products.product_by_id', id=search_string))

    product_data = DB_Commands.find_product_by_id(search_string)
    for data in product_data:
        product=data

    return render_template("products/edit_product.html", data=product, form=edit_product_form)


@bp.route('/lookup/<id>/delete_product', methods=('GET', 'POST'))
def delete_product_by_id(id):
    """
    Route for deleting product by id
    :param id: represents the numerical id of the product in the database
    :return: rendered template
    """
    edit_product_form = ProductForm(request.form)
    try:
        search_string = id.data['search']
    except:
        search_string = str(id)
        id = SearchProductById(request.form)
        id.data['search'] = search_string
    
    product_data = DB_Commands.find_product_by_id(search_string)
    for data in product_data:
        product=data

    if request.method == "POST":
        DB_Commands.delete_product(search_string)
        return redirect(url_for('products.products'))

    return render_template("products/delete_product.html", data=product, form=edit_product_form)