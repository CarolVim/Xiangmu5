from flask_wtf.file import FileAllowed, FileRequired
from wtforms import Form, StringField, PasswordField, FileField, IntegerField
from wtforms.validators import InputRequired, Length, NumberRange


class LoginForm(Form):
    username = StringField(
        label='用户名',
        validators=[
            InputRequired('用户名必填'),
            Length(4, 20, '用户长度未4到20')
        ]
    )
    password = PasswordField(
        label='密码',
        validators=[
            InputRequired('密码必填'),
            Length(6, 30, '密码长度为6到9')
        ]
    )


class RegisterForm(Form):
    username = StringField(
        label='用户名',
        validators=[
            InputRequired('用户名为必填项'),
            Length(6, 15, '密码长度为4到20')
        ]
    )
    password1 = StringField(
        label='密码',
        validators=[
            InputRequired('密码为必填项'),
            Length(6, 30, '密码长度为6到9')
        ]
    )
    password2 = StringField(
        label='密码',
        validators=[
            InputRequired('密码为必填项'),
            Length(6, 30, '密码长度为6到9')
        ]
    )
    phone = StringField(validators=[Length(0, 100, message='手机号码为1-100位')])


class ApplyForm(Form):
    name = StringField(
        label='提交个人或则团队姓名',
        validators=[
            InputRequired('个人或者团队名称为必填项'),
            Length(0, 10, '长度为6到9')
        ]
    )
    cost = IntegerField(
        label='提交预算',
        validators=[
            InputRequired('为必填项'),
            NumberRange(min=-0x8000000000000000, max=0x7fffffffffffffff)
        ]

    )
    plan = StringField(
        label='提交个人或者团队计划',
        validators=[
            InputRequired('个人或者团队名称为必填项'),
            Length(0, 10, '长度为6到9')
        ]

    )
    img=FileField(
        validators=[
                FileRequired(),
                FileAllowed(["jpg", "png", "jpeg"])
        ]
    )
    zip=FileField(
        validators=[
            FileRequired(),
            FileAllowed(["zip","rar"])
        ]
    )
