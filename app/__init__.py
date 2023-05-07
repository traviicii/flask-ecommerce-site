from flask import Flask
from config import Config
from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager
from .auth.routes import auth
from .api import api
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
cors = CORS(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# login_manager.login_view = 'auth.loginPage'

# Register your blueprints here
app.register_blueprint(auth)
app.register_blueprint(api)


from . import routes
from . import models