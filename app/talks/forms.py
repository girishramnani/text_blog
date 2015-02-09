from flask.ext.wtf.form import Form
from wtforms.fields.core import StringField, DateField
from wtforms.fields.simple import SubmitField
from wtforms.validators import Required, DataRequired, optional

__author__ = 'Girish'


class TalkForm(Form):
    title = StringField("Title :",validators=[DataRequired()])
    discription = StringField("Discription :",validators=[DataRequired()])
    slides = StringField("Slides: ",validators=[optional()])
    video = StringField("Videos: ",validators=[optional()])
    submit=SubmitField("Add talk")






