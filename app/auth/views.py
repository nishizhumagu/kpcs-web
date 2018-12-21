#!user/bin/env python3
# -*-coding:utf-8-*-
from flask import render_template, session, redirect, url_for, request, flash
from . import auth
from .forms import LoginForm
from .. import db
from app.models import User
from flask_login import login_required, login_user, logout_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(pl_num=form.pl_num.data).first()
        if user is not None and user.verify_password(form.pl_num.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash(u'用户名或密码错误')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('注销成功')
    return redirect(url_for('main.index'))
