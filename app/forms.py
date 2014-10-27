from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, StringField, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    email = StringField('email')
    password = PasswordField('password')
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(Form):
    email = StringField('email')
    password = PasswordField('password')
    valid_password = PasswordField('valid_password')