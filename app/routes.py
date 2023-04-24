from app import app
from flask import render_template, flash, redirect, request, url_for
from .models import Inventory, User
from app.auth.forms import InventoryField



app.secret_key = 'my_secret_key'

@app.route('/')

@app.route('/index')
def base():
    products = Inventory.query.all()
    admin = User.is_admin()
    print(admin)
    return render_template('index.html', products=products, admin=admin)

@app.route('/cart')
def cart():
    """shopping cart page

    Returns:
        _type_: shows the user their current items they have placed in their cart
    """
    return render_template('cart.html')

@app.route('/remove/<int:prodid>')
def removeItem(prodid):
    deleteme = Inventory.query.filter_by(id=prodid).first()
    deleteme.deleteFromDB()
    return render_template('index.html')

@app.route('/edititem/<int:prodid>')
def editItem(prodid):
    item = Inventory.query.filter_by(id=prodid).first()
    if item:
        form = InventoryField()
        if request.method == 'POST':
            if form.validate():
                print('im right here')
                product_name = form.product_name.data
                price = form.price.data
                description = form.description.data
                image = form.image.data
                image2 = form.image2.data
                image3 = form.image3.data
                image4 = form.image4.data

                product = Inventory(product_name, price, description, image, image2, image3, image4)
                print('Product instance is created')
                product.saveToDB()
                flash('Product added to Inventory!', 'success')
                return render_template('index.html', form=form)
    return render_template('index.html', form=form)




#flask run --port 8000
