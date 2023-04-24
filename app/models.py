from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin, current_user

db = SQLAlchemy()

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default=datetime.utcnow())
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, first_name, last_name, email):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def is_admin():
        return current_user.is_authenticated and current_user.is_admin
 
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()


class Inventory(db.Model):

    id = db.Column(db.Integer, primary_key = True, unique=True)
    product_name = db.Column(db.String(50), nullable = False, unique = True)
    price = db.Column(db.Float, nullable = False)
    # quantity = db.Column(db.Integer, primary_key = True, autoincrement = False)
    description = db.Column(db.String(500), nullable = False)
    image = db.Column(db.String(500), nullable = False)
    image2 = db.Column(db.String(500)) #optional
    image3 = db.Column(db.String(500)) #optional
    image4 = db.Column(db.String(500)) #optional

    def __init__(self, product_name, price, description, image, image2, image3, image4):
        self.product_name = product_name
        self.price = price
        self.description = description
        self.image = image
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
 
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()


class Cart(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False, autoincrement = False)
    prod_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable = False, autoincrement = False)

    def __init__(self, user_id, prod_id):
        self.user_id = user_id
        self.prod_id = prod_id

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    total_price = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, total_price):
        self.user_id = user_id
        self.total_price = total_price
