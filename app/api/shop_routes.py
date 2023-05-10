from . import api
from ..models import Inventory, Cart
from flask import abort, request #can send different types of http errors
from .apiauthhelper import token_auth


@api.get('/products')
def getProductsAPI():
    products = Inventory.query.all()
    return {
        'status': 'ok',
        'results': len(products),
        'products': [p.to_dict() for p in products]
    }

@api.get('/products/<int:product_id>')
def getProductAPI(product_id):
    product = Inventory.query.get(product_id)
    if product :
        return {
            'status': 'ok',
            'results': 1,
            'product': product.to_dict()
        }
    else:
        return {
                'status': 'not ok',
                'message': "The product you're looking for does not exist."
            }, 404

@api.get('/cart')
@token_auth.login_required
def getCartAPI():
    print('hey')
    user = token_auth.current_user()
    print(user)
    return {
        'status': 'ok',
        'cart': [Inventory.query.get(c.prod_id).to_dict() for c in Cart.query.filter_by(user_id=user.id).all()]
    }

@api.post('/cart')
@token_auth.login_required
def addToCartAPI():
    user = token_auth.current_user()
    data = request.json

    product_id = data['product_id']
    product = Inventory.query.get(product_id)

    if product:
        cart_item = Cart(user.id, product.id)
        cart_item.saveToDB()

        return {
            'status': 'ok',
            'message': f'Successfully added {product.product_name} to your cart!'
        }
    else:
        return{
            'status': 'not ok',
            'message': 'That product does not exist!'
        }
    
@api.delete('/cart/<int:product_id>')
@token_auth.login_required
def removeFromCartAPI(product_id):
    user = token_auth.current_user()
    product = Inventory.query.get(product_id)
    item = Cart.query.filter_by(user_id=user.id).filter_by(prod_id=product_id).first()
    if item:
        item.deleteFromDB()
        return {
            'status': 'ok',
            'message': f'Removed {product.product_name} from cart.'
        }, 200
    else:
        return {
            'status': 'not ok',
            'message': 'Item does not exist in cart.'
        }