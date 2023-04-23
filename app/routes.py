from app import app
from flask import render_template



app.secret_key = 'my_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def base():
    return render_template('index.html')

@app.route('/cart')
def cart():
    """shopping cart page

    Returns:
        _type_: shows the user their current items they have placed in their cart
    """
    return render_template('cart.html')



#flask run --port 8000
