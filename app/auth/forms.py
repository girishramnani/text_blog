from wtforms.fields.core import StringField, BooleanField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import Required, DataRequired, Length, Email

__author__ = 'Girish'

from flask.ext.wtf import Form


class LoginForm(Form):
    email = StringField("Email",validators=[DataRequired("Cannot be empty"),Length(1,64),Email()])
    password= PasswordField("Password",validators=[DataRequired("Cannot be empty")])
    remember_me =BooleanField("Keep me logged in")
    submit = SubmitField("log In")

