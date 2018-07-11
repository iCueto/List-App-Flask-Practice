from app import db

from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column('first_name', db.String(20))
    last_name = db.Column('last_name', db.String(20))
    nickname = db.Column('nickname', db.String(20))
    email = db.Column('email', db.String(20))

    lists = db.relationship('List', backref='creator', lazy=True)


class List(db.Model):
    __tablename__ = 'lists'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('title', db.String(100))
    picture_url = db.Column('picture_url', db.String(200))
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    creator_id = db.Column('creator_id', db.Integer, db.ForeignKey('users.id'))

    items = db.relationship('Item', backref='list', lazy=True)


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('title', db.String(100))
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)
    updated_at = db.Column('updated_at', db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    list_id = db.Column('list_id', db.Integer, db.ForeignKey('lists.id'))
