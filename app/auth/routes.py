from flask.globals import request
from flask.helpers import flash, url_for
from app.auth.forms import LoginForm
from flask import redirect
__author__ = 'Girish'


from flask import render_template

from app.auth import auth
from  flask.ext.login import login_user, login_required, logout_user
from app.model import User
@auth.route('/login', methods=["GET","POST"])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for("auth.login"))
        print("out")
        login_user(user,form.remember_me.data)
        return redirect(url_for("talks.index"))
    return render_template("login2.html",forms=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("talks.index"))
