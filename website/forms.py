from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import Required, NumberRange
from models import User

class Login_form(Form):
  username = StringField('Usuario')
  password = HiddenField('Contraseña')

class Create_form(Form):
  username = StringField('Usuario')
  password = PasswordField('Contraseña')
  def validate_username(form,field):
    username = field.data
    user = User.query.filter_by(username = username).first()
    if user is not None:
      raise validators.ValidationError("Usuario ya se encuentra usado")
