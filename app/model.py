from werkzeug.security import generate_password_hash, check_password_hash

__author__ = 'Girish'

from flask.ext.login import UserMixin
from datetime import datetime
from app import db,login_manager
class User(UserMixin,db.Model):

    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),nullable=False,unique=True,index=True)
    username = db.Column(db.String(64),nullable=False,unique=True,index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    bio = db.Column(db.Text())
    location  =db.Column(db.String(64))
    member_since= db.Column(db.DateTime(),default=datetime.utcnow())
    avatar_hash = db.Column(db.String(32))
    talks = db.relationship('Talk',backref='author',lazy='dynamic')


    @property
    def password(self):
        raise ArithmeticError("not a readable attribute")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)


    def verify(self,password):
        return check_password_hash(self.password_hash,password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Talk(db.Model):
    __tablename__ ='talks'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128),nullable=False)
    description = db.Column(db.Text())
    slides = db.Column(db.Text())
    video = db.Column(db.Text())
    date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
