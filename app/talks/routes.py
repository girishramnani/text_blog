__author__ = 'Girish'


from flask import render_template
from app.model import User
from app.talks import talks

@talks.route('/index')
@talks.route('/')
def index():
    return render_template(r"index.html",title="Talks")



@talks.route('/user/<user>')
def user_name(user):
    temp  =User.query.filter_by(username=user).first_or_404()
    return render_template("user.html",user=temp,title="Talks")

