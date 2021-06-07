from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired, Length, NumberRange


class ApplyForm(Form):
    pro_name = StringField(
        label='项目名称',
        validators=[
            InputRequired('项目名称为必填项'),
            Length(6, 15, '长度为4到20')
        ]
    )
    pro_cost = StringField(
        label='预算',
        validators=[
            InputRequired('预算为必填项'),
            NumberRange(min=-0x8000000000000000, max=0x7fffffffffffffff)
        ]
    )
    pro_status= StringField(
        label='项目状态',
        validators=[
            InputRequired('项目状态为必填项'),
            Length(6, 30, '长度为6到9')
        ]
    )