from werkzeug.security import generate_password_hash, check_password_hash

from exts import db
from datetime import datetime

#管理员表
class Admin(db.Model):
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),unique=True)
    _password = db.Column(db.String(100), nullable=False)  # 密码不能为空
    email=db.Column(db.String(50))
    role=db.Column(db.String(50))
    def __init__(self,name,_password,email,role=role):
        self.name=name
        self.password=_password
        self.email=email
        self.role=role

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,raw_password):
        self._password=generate_password_hash(raw_password)
    def check_password(self,raw_password):
        result=check_password_hash(self.password,raw_password)
        return result


