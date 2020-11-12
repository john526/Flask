from app import db


class User(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {} > : ".format(self.username)




#https://ondras.zarovi.cz/sql/demo/

"""
error : sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:sqllite

Start a python shell in your virtual environment and run the following:

import sqlalchemy.dialects.sqlite
"""
