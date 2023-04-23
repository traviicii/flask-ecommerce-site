from app import app
from flask import render_template



app.secret_key = 'my_secret_key'

@app.route('/index')
def base():
    return render_template('index.html')

@app.route('/signup')
def sign_up():
    """sign up page

    Returns:
        form: takes new user info
    """
    return render_template('signup.html')

@app.route('/signin')
def signin():
    """allows the user to sign in

    Returns:
        form: signs the user in
    """
    return render_template('signin.html')

@app.route('/cart')
def cart():
    """shopping cart page

    Returns:
        _type_: shows the user their current items they have placed in their cart
    """
    return render_template('cart.html')
