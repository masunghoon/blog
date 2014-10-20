from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, StringField, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    id = StringField('id')
    password = PasswordField('password')
    remember_me = BooleanField('remember_me', default=False)