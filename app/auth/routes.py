__author__ = 'Girish'


from flask import render_template

from app.auth import auth

@auth.route('/login')
def login():
    return render_template("login.html")