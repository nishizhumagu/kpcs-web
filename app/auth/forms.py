#!user/bin/env python3
# -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp


class LoginForm(FlaskForm):
    pl_num = StringField(u'警号', validators=[Length(min=6, max=6, message=u'请输入正确警号')])
    password = PasswordField(u'密码', validators=[
        DataRequired(),
        Length(min=6, max=20, message=u'密码长度必须在6-20个字符之间')])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')
