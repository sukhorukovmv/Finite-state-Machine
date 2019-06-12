from sqlalchemy import event
from datetime import datetime

from app.database import db
import re

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    secondName = db.Column(db.String(100), nullable=False, unique=True)
    firstName = db.Column(db.String(100) )
    middleName = db.Column(db.String(100))
    nickname = db.Column(db.String(140), unique=True)
    created_at = db.Column(db.DateTime, default=datetime:now())

#    comments = db.relationship('Comment', backref='entity')
#    def __init__(self, *args, **kwargs):
#        super(Users, self).__init__(*args, **kwargs)
#        self.nickname = generate_nickname()

#    def generate_nickname(self):
#        if self.title:
#            self.nickname = slugify(self.title)

#    def __repr__(self):
#        return '<Post id'

#    def __str__(self):
#        return self.name

