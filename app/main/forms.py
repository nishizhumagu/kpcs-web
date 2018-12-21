#!user/bin/python3
# -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp


class UserForm(FlaskForm):
    pl_num = StringField(u'警号', validators=[Length(min=6, max=6, message=u'请输入正确警号')])
    real_name = StringField(u'真实姓名', validators=[Length(min=2, max=4, message=u'请输入正确姓名')])
    pl_station = StringField(u'工作单位', validators=[DataRequired()])  # 以后要弄成标签选择
    password = PasswordField(u'密码', validators=[
        DataRequired(),
        Length(min=6, max=20, message=u'密码长度必须在6-20个字符之间')])
    password_eq = PasswordField(u'请确认密码', validators=[
        DataRequired(),
        EqualTo('password', message=u'两次密码不一致'),
        Length(min=6, max=20, message=u'密码长度必须在6-20个字符之间')])
    phone_num = StringField(
        u'联系方式',
        validators=[Regexp(r'^(13[0-9]|14[5|7]|15[0-3|5-9]|17[0|3|5-8]|18[0-9]|166|198|199|147)\d{8}$')])
    submit = SubmitField(u'注册')


class KeyPerson(FlaskForm):
    id = StringField(u'身份证号', validators=[Regexp(r'^[1-6]\d{5}[1-2]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{4}$')])
    name = StringField(u'姓名', validators=[DataRequired()])
    gender = BooleanField(u'性别', validators=[DataRequired()])
    ctrl_reason = TextAreaField(u'列管原因', validators=[DataRequired()])
    pl_station = StringField(u'列管单位', validators=[DataRequired()])


