from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, StringField, PasswordField, TextAreaField
from wtforms.validators import Required, Length

class LoginForm(Form):
    email = StringField('email')
    password = PasswordField('password')
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(Form):
    email = StringField('email')
    password = PasswordField('password')
    valid_password = PasswordField('valid_password')


class EditForm(Form):
    nickname = StringField('nickname')
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])