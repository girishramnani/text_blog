from flask.ext.login import login_required, current_user
from flask.helpers import url_for
from app.talks.forms import TalkForm

__author__ = 'Girish'


from flask import render_template,redirect
from app.model import User,Talk
from app.talks import talks
from app import db
@talks.route('/index')
@talks.route('/')
def index():
    talks_data = Talk.query.order_by(Talk.date).all()
    print(talks_data[1].title)
    return render_template(r"index.html",title="Talks",talks=talks_data)



@talks.route('/user/<user>')
def user_name(user):
    temp  =User.query.filter_by(username=user).first_or_404()
    return render_template("user.html",user=temp,title="Talks")



@talks.route('/form', methods=['GET','POST'])
@login_required
def form():
    Talk_form = TalkForm()
    if Talk_form.validate_on_submit():
        talk = Talk()
        talk.description = Talk_form.discription.data
        talk.title = Talk_form.title.data
        talk.slides = Talk_form.slides.data
        talk.video = Talk_form.slides.data
        talk.author = current_user
        db.session.add(talk)
        db.session.commit()
        return redirect(url_for("talks.index"))

    return render_template("form.html",forms=Talk_form)

