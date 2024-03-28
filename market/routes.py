from market import app,db
from market.models import Item
from  flask import render_template

@app.route('/')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():
  items = db.session().execute(db.select(Item).order_by(Item.id)).scalars()
  return render_template('market.html',items = items)