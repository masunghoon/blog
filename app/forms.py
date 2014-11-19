from flask.ext.wtf import Form
from wtforms import TextField,StringField,PasswordField, BooleanField,TextAreaField
from wtforms.validators import DataRequired,Required, Length
from app.models import User

class LoginForm(Form):
    email = StringField('email',validators=[DataRequired()])
    password = PasswordField('password')
    # openid = TextField('openid',validators=[Required()])
    remember_me =BooleanField('remember_me',default=False)

class RegisterForm(Form):
    email = StringField('email')
    password = PasswordField('password')
    valid_password = PasswordField('valid_password')


class EditForm(Form):
    nickname = StringField('nickname')
    about_me = TextAreaField('about_me', validators = [Length(min=0,max=140)])

    def __init__(self, original_nickname, *args, **kwaegs):
        Form.__init__(self, *args, **kwaegs)
        self.original_nickname = original_nickname


    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])

