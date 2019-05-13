from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']= '50eb51cfa4098f26588f83086fa28229'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres@localhost/synaptic_db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message_category = 'info'

from synaptic import routes
