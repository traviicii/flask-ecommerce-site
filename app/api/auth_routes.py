from . import api
from ..models import User
from flask import request
from werkzeug.security import check_password_hash
from .apiauthhelper import basic_auth, token_auth

@api.post('/signup')
def signUpAPI():
    '''
    Expected request body:

    '''
    data = request.json

    username = data['username']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']

    user = User.query.filter_by(username = username).first()
    if user:
        return {
            'status': 'not ok',
            'message': 'That username already exists, please choose a different one.'
        }, 400
    user = User.query.filter_by(email = email).first()
    if user:
        return {
            'status': 'not ok',
            'message': 'That email already exists, please choose a different one.'
        }, 400


    user = User(username, password, first_name, last_name, email)
    user.saveToDB()
    return {
        'status': 'ok',
        'message': 'Account successfully created!'
    }, 201

@api.post('/login')
@basic_auth.login_required
def loginAPI():
    '''
    Expected request body:

    '''
    # data = request.json

    # username = data['username']
    # password = data['password']


    # user = User.query.filter_by(username = username).first()
    # if user:
    #     #Check password
    #     if check_password_hash(user.password, password):
    #         #if valid give token


    return {
        'status': 'ok',
        'message': 'You have successfully logged in.',
        'data': basic_auth.current_user().to_dict()
    }, 200
    #     else: {
    #         'status': 'not ok',
    #         'message': 'Incorrect username/password.',
    #         'data': user.to_dict()
    #     }
    # else: {
    #     'status': 'not ok',
    #     'message': "That user doesn't exist. Please sign up.",
    # }, 401

