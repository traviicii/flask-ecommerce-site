from . import api
from ..models import Inventory
from flask import abort #can send different types of http errors

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
            'products': product.to_dict()
        }
    else:
        return {
                'status': 'not ok',
                'message': "The product you're looking for does not exist."
            }, 404
