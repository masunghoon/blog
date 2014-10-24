from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password')
    #openid = TextField('openid', validators= [Required()])
    remember_me = BooleanField('remember_me', default=False)


class RegisterForm(Form):
    email = StringField('email')
    password = PasswordField('password')
    valid_password = PasswordField('valid_apssword')