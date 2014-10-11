from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    # openid = TextField('openid', validators= [Required()])
    id = StringField('id')
    password = PasswordField('password')
    remember_me = BooleanField('remember_me', default=False)