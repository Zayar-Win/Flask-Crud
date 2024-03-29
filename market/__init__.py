from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_session import Session 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '475c5f7571a7ccc4db093f3a'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from market import routes