from market import app,db
from market.models import Item,User
from  flask import render_template,request,redirect,url_for,flash
from market.forms import RegisterForm,LoginForm,PurchaseForm,SellForm
from flask_login import login_user,logout_user,login_required,current_user

@app.route('/')
def home_page():
  return render_template('home.html',greeting='hello world')

@app.route('/market',methods=['GET','POST'])
@login_required
def market_page():
  purchaseForm = PurchaseForm()
  sellForm = SellForm()
  if request.method == 'POST':
    purchase_item = request.form.get('item')
    item = Item.query.filter_by(id=purchase_item).first()
    if item:
      if current_user.can_buy(item):
        item.buy(current_user)
        flash(f'You purchase {item.name}',category='success')
      else:
        flash(f'You don\'t have enough money to purchase.',category='success')
    sell_item = request.form.get('sell_item')
    print(sell_item)
    item = Item.query.filter_by(id=sell_item).first()
    if item:
      if current_user.can_sell(item):
        item.sell(current_user)
        flash('You sold this item.Check your balance.')
    return redirect(url_for('market_page'))
  if request.method == 'GET':
    items = db.session().query(Item).filter_by(user_id=None).all()
    ownedItems = []
    if current_user:
      ownedItems = Item.query.filter_by(user_id=current_user.id).all()
    return render_template('market.html',items = items,purchaseForm=purchaseForm,ownedItems=ownedItems,sellForm=sellForm)
    

@app.route('/register',methods=['GET','POST'])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(name=form.name.data,email=form.email.data,password_hash=form.password.data,budget=10000)
    db.session().add(user)
    db.session().commit()
    login_user(user)
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

@app.route('/logout')
def logout():
  logout_user()
  flash('See you later.',category='success')
  return redirect(url_for('home_page'))