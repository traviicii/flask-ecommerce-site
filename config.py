import os

class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
<<<<<<< HEAD
    SECRET_KEY = os.environ.get('SECRET_KEY')
=======
    #SECRET_KEY = os.environ.get('SECRET_KEY')
>>>>>>> 8c78cf8315b9357938ca679578282dbae4315ca7
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False