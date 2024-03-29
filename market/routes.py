from market import app,db
from market.models import Item,User
from  flask import render_template,request,redirect,url_for,flash
from market.forms import RegisterForm,LoginForm
from flask_login import login_user

@app.route('/')
def home_page():
  return render_template('home.html',greeting='hello world')

@app.route('/market')
def market_page():
  items = db.session().query(Item).all()
  return render_template('market.html',items = items)

@app.route('/register',methods=['GET','POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(name=form.name.data,email=form.email.data,password_hash=form.password.data,budget=10000)
    db.session().add(user)
    db.session().commit()
    flash(message='User register success.',category='success')
    return redirect(url_for('home_page'))
  
  return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login_page():
  form = LoginForm()
  if form.validate_on_submit():
    attempted_user = User.query.filter_by(email=form.email.data).first()
    if attempted_user and attempted_user.check_password(form.password.data) : 
      login_user(attempted_user)
      flash('Welcome Back',category='success')
    return redirect(url_for('home_page'))

  return render_template('login.html',form=form)