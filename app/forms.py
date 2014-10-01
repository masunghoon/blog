from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    id = StringField('id', validators=[DataRequired()])
    password = PasswordField('password')
    # openid = TextField('openid', validators= [Required()])
    remember_me = BooleanField('remember_me', default=False)