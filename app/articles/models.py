from sqlalchemy import event
from datetime import datetime

from app.database import db
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

import re

def slugify(s):
    pattern = r'[^\w+]'

class Post(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

#    comments = db.relationship('Comment', backref='entity')
    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)
        self.nickname = generate_nickname()

    def generate_nickname(self):
        if self.title:
            self.nickname = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

