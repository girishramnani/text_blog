__author__ = 'Girish'


from flask import render_template

from app.talks import talks
@talks.route('/')
def index():
    return render_template(r"index.html")



