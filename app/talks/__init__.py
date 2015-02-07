__author__ = 'Girish'

from flask import Blueprint
talks = Blueprint('talks',__name__)
print("here in talks")
from app.talks import routes