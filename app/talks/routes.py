from flask.ext.login import login_required, current_user
from flask.helpers import url_for, flash
from app.talks.forms import TalkForm

__author__ = 'Girish'


from flask import render_template,redirect
from app.model import User,Talk
from app.talks import talks
from app import db
import random,string
def random_creater():
    return random.choice(string.ascii_uppercase)

@talks.route('/index')
@talks.route('/')
def index():
    talks_data = Talk.query.order_by(Talk.date).all()

    print(talks_data[1].title)
    return render_template(r"index.html",title="Talks",talks=talks_data,func=random_creater,data="TECH TALKS",rows=5)



@talks.route('/user/<user>')
def user_name(user):
    temp  =User.query.filter_by(username=user).first_or_404()
    return render_template("user.html",user=temp,title="Talks")

@talks.route('/background')
def clock():
    return render_template("background.html")





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
        flash("")
        return redirect(url_for("talks.index"))

    return render_template("form.html",forms=Talk_form)



@talks.route("/talks/<int:tid>")
def perma_link(tid):
    T = Talk.query.filter_by(id=tid).first()
    if T is None:
        return render_template("404.html")
    return render_template("talk.html",data = T)
