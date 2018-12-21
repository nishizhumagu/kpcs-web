#!user/bin/python3
# -*-coding:utf-8-*-
from flask import render_template, session, redirect, url_for, request, flash
from . import main
from .forms import UserForm
from .. import db
from app.models import User
from flask_login import login_required, login_user, logout_user


@main.route('/register', methods=["GET", "POST"])
def register():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(pl_num=form.pl_num.data).first()
        if user is None:
            user = User(
                pl_num=form.pl_num.data, real_name=form.real_name.data,
                pl_station=form.pl_station.data, password=form.password.data,
                phone_num=form.phone_num.data
            )
            db.session.add(user)
            flash(u'注册成功!')
            redirect(url_for('auth.login'))
        else:
            return redirect(url_for('main.index'))
    return render_template('register.html', form=form)






@main.route('/')
# @login_required
def index():
    return render_template('index.html')


