from market import db
from sqlalchemy.orm import Mapped,mapped_column

#Item model
class Item(db.Model):
  id : Mapped[int] = mapped_column(primary_key=True)
  name : Mapped[str] = mapped_column(unique=True)
  barcode : Mapped[str]
  price : Mapped[int]