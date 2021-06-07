from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from exts import db


class User(db.Model):
    __tablename__='user'
    uid=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),nullable=True)#账号名称
    _password=db.Column(db.String(100),nullable=False)#账号密码
    phone = db.Column(db.String(50), nullable=False, unique=True)
    def __init__(self, username, password, phone):
        self.username = username
        self.password = password
        self.phone = phone
    @property
    def password(self):
        return self._password

    # 设置密码
    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)

        return result


class XiangMu(db.Model):
    __tablename__='xiangmu'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    picture=db.Column(db.String(255))
    detail=db.Column(db.String(255))
    applyId=db.Column(db.Integer,db.ForeignKey('user.uid'))
    applydate=db.Column(db.DateTime, index=True, default=datetime.now)
    finishdate = db.Column(db.DateTime)

class Apply(db.Model):
    __tablename__='apply'
    id=db.Column(db.Integer,primary_key=True)
    applyId=db.Column(db.Integer,db.ForeignKey('user.uid'),unique=True)
    name=db.Column(db.String(50))
    content=db.Column(db.String(255))
    cost=db.Column(db.String(50))
    level=db.Column(db.String(255),default='0')
    status=db.Column(db.String(255),default='申请中')
    img=db.Column(db.String(255))
    zip=db.Column(db.String(255))
    applyDate=db.Column(db.DateTime, index=True, default=datetime.now)

class Record(db.Model):
    __tablename__='record'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    userId=db.Column(db.Integer,db.ForeignKey('user.uid'))
    content=db.Column(db.String(255))
    # answer=db.Column(db.String(255))#答复
    addDate=db.Column(db.DateTime,index=True,default=datetime.now)


