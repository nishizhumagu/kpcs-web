#!user/bin/env python3
# -*-coding:utf-8-*-
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, index=True)

    @property
    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pl_num = db.Column(db.String(6), unique=True, index=True)
    real_name = db.Column(db.String(4), index=True)
    pl_station = db.Column(db.String, index=True)
    password_hash = db.Column(db.String)
    phone_num = db.Column(db.String(11), unique=True)
    register_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError(u'密码不允许读取！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {first}:{second}>'.format(first=self.pl_num, second=self.real_name)


class KeyPerson(db.Model):
    __tablename__ = 'keypersons'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_num = db.Column(db.String(18), index=True, unique=True)
    name = db.Column(db.String(4), index=True)
    gender = db.Column(db.Boolean)
    ctrl_reason = db.Column(db.Text)
    pl_station = db.Column(db.String)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    change_time = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now)
    # activity = db.relationship('activities', backref='keyperson', lazy='dynamic')


class Activity(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ac_content = db.Column(db.String)
    ac_time = db.Column(db.DateTime, index=True)
    ac_mode = db.Column(db.String(2))
    feedback = db.Column(db.Text)
    # keyperson_id = db.Column(db.String, db.ForeignKey('keypersons.id', ondelete='CACSE'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

