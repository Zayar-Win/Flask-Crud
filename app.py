from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home_page():
  items = [
    {
      'id':'1',
      'name' : 'IPhone',
      'barcode' : '123456',
      'price' : 10000
    },
    {
      'id':'2',
      'name' : 'IPhone11',
      'barcode' : '1233256',
      'price' : 1000
    },
    {
      'id':'3',
      'name' : 'MacBook',
      'barcode' : '3f23456',
      'price' : 1000000
    },
    {
      'id':'4',
      'name' : 'MacBookAir',
      'barcode' : '12345rer6',
      'price' : 10000
    },
  ]
  return render_template('home.html',items = items)