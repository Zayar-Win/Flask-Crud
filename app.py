from market import app,db
from market.models import Item

# with app.app_context():
#   item1 = Item(name='Item1',barcode='12345678',price=10000)
#   item2 = Item(name='Item2',barcode='12345678',price=10000)
#   item3 = Item(name='Item3',barcode='12345678',price=10000)
#   item4 = Item(name='Item4',barcode='12345678',price=10000)
#   item5 = Item(name='Item5',barcode='12345678',price=10000)
#   db.session().add_all([item1,item2,item3,item4,item5])
#   db.session().commit()

if __name__ == '__main__':
  app.run(debug=True)