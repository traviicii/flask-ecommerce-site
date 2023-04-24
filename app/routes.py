from app import app
from flask import render_template, flash
from .models import Inventory



app.secret_key = 'my_secret_key'

@app.route('/')

@app.route('/index')
def base():
    products = Inventory.query.all()
    return render_template('index.html', products=products)

@app.route('/cart')
def cart():
    """shopping cart page

    Returns:
        _type_: shows the user their current items they have placed in their cart
    """
    return render_template('cart.html')





#flask run --port 8000
