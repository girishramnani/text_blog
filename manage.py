__author__ = 'Girish'

import os
from app import create_app

from flask.ext.script import Manager
app = create_app("development")
manager = Manager(app)
from app import db
from app.model import User

@manager.command
def adduser(email,username,admin=False):
    from getpass import getpass
    password=getpass()
    password2 =getpass(prompt="Confirm: ")
    if password !=password2:
        import sys
        sys.exit("Error : password do not match")

    db.create_all()
    user = User(email=email,username=username,password=password,is_admin=admin)
    db.session.add(user)
    db.session.commit()
    print("done")
if __name__ =="__main__":
    manager.run()
