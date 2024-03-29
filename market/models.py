from market import login_manager
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from typing import List
from flask_login import UserMixin
from market import bcrypt
from market import db

@login_manager.user_loader
def user_loader(user_id):
  return User.query.filter_by(id=int(user_id)).first()

#Item model
class Item(db.Model):
  id : Mapped[int] = mapped_column(primary_key=True)
  name : Mapped[str] = mapped_column(unique=True)
  barcode : Mapped[str]
  price : Mapped[int]
  user_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
  owner : Mapped["User"] = relationship(back_populates="items")

#User Model
class User(db.Model,UserMixin):
  id: Mapped[int] = mapped_column(primary_key=True)
  name : Mapped[str] = mapped_column(unique=True)
  email : Mapped[str] = mapped_column(unique=True)
  password : Mapped[str]
  budget : Mapped[int]
  items : Mapped[List["Item"]] = relationship(back_populates="owner")

  @property
  def password_hash(self):
    return self.password
  
  @password_hash.setter
  def password_hash(self,plain_text_password):
    self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
  
  def check_password(self,plain_text_password):
    return bcrypt.check_password_hash(self.password,plain_text_password)
