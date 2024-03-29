from flask_wtf import FlaskForm
from wtforms.validators import Length,Email,DataRequired,ValidationError
from wtforms.fields import StringField,PasswordField,SubmitField
from market.models import User
class RegisterForm(FlaskForm):
  def validate_name(form,field):
    user = User.query.filter_by(name=field.data).first()
    if user:
      raise ValidationError('User Name already exists.')
  def validate_email(form,field):
    user = User.query.filter_by(email=field.data).first()
    if user:
      raise ValidationError('Email already exists.')
  name = StringField(label='Name',validators=[DataRequired(),Length(1,30)])
  email = StringField(label='Email',validators=[Email(),DataRequired()])
  password = PasswordField(label='Password',validators=[Length(6,20),DataRequired()])
  submit = SubmitField(label='Create User')

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[Email(),DataRequired()])
  password = PasswordField('Password',validators=[DataRequired(),Length(6,30)])
  submit = SubmitField('Login')

class PurchaseForm(FlaskForm):
  submit = SubmitField('Purchase')
class SellForm(FlaskForm):
  submit = SubmitField('Sell')

