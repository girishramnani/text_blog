__author__ = 'Girish'


from flask import render_template

from app.talks import talks
print("Sdf")
@talks.route('/')
def index():
    return render_template(r"index.html")



