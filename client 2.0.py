from flask import Flask
from flask_login import UserMixin, current_user, login_manager
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__,  template_folder='../templates')
CSRFProtect(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, 
                   primary_key = True)
    username = db.Column(db.String(20),
                         unique = True, 
                         nullable = False)
    email = db.Column(db.String(120), 
                      unique = True, 
                      nullable = False)
    password = db.Column(db.String(60), 
                         nullable = False)