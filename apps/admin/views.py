import datetime
from functools import wraps

from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import config
from apps.admin.models import Admin
from apps.front import XiangMu, Apply, User
from .data import SourceData
from exts import db

bp = Blueprint("admin", __name__, url_prefix='/admin')
source = SourceData()


def admin_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@bp.route("/login.html", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        user = request.form.get('username')
        pwd = request.form.get('password')
        users = Admin.query.filter_by(name=user).first()
        print(users)
        if users:
            if user == users.name and not users.check_password(pwd):
                session["admin"] = user
                session['user_id'] = users.id
                print('登陆成功！')
                return redirect(url_for('admin.HT'))
            else:
                return render_template('admin/login.html')
        else:
            return render_template('admin/login.html')


@bp.route('/index.html')
@admin_login
def HT():
    return render_template('admin/index.html')


@bp.route('/project_List.html')
@admin_login
def project_shenhe():
    Xm = Apply.query.filter_by(status='开展').all()
    return render_template('admin/project_list.html', Xm=Xm)

@bp.route('/project_guidang.html')
@admin_login
def project_guidang():
    Xm = Apply.query.filter_by(status='项目完成').all()
    return render_template('admin/project_guidang.html', Xm=Xm)

@bp.route('/project_shenhe.html')
@admin_login
def project_list():
    Xm = Apply.query.filter_by(status='申请中').all()
    return render_template('admin/project_shenhe.html', Xm=Xm)


@bp.route('/proEdit.html')
@admin_login
def proEdit():
    Id = request.args.get('pId')
    proList = Apply.query.filter_by(id=Id).first()
    return render_template('admin/proEdit.html', proList=proList)


@bp.route('/Edit.html', methods=['GET', 'POST'])
@admin_login
def Edit():
    if request.method == 'POST':
        pId = request.args.get('pId')
        print(pId)
        now = datetime.datetime.now()
        cost = request.form['pro_cost']
        print('cost:', cost)
        pro_name = request.form['pro_name']
        status = request.form['pro_status']
        print('status:', status)
        Apply.query.filter_by(id=int(pId)).update({
            'name': pro_name,
            'cost': cost,
            'status': status,
            'applyDate': now
        })
        print('更新成功')
        db.session.commit()
        db.session.close()
        history = Apply.query.filter_by(status='项目归档').first()
        userId=session.get(config.FRONT_CUSTOMER_ID)
        names = history.name
        picture = history.img
        detail = history.content
        applyDate = history.applyDate
        X = XiangMu(
            name=history.name,
            picture=history.img,
            detail=history.content,
            applyId=userId,
            applydate=history.applyDate
        )
        db.session.add(X)
        db.session.commit()
        if status == '项目归档':
            userId = session.get(config.FRONT_CUSTOMER_ID)
            XiangMu.query.filter_by(applyId=userId).update(
                {'finishdate': now}
            )
            db.session.commit()
            db.session.close()
            return render_template(url_for('admin.proEdit'))
        return redirect(url_for('admin.proEdit'))


@bp.route('/ApplyList.html')
@admin_login
def Apply_list():
    Xm = Apply.query.all()
    return render_template('admin/applyList.html', Xm=Xm)


@bp.route('/userlist.html')
@admin_login
def userList():
    keywords = request.args.get('keywords', '', type=str)
    page = request.args.get('page', 1, type=int)
    if keywords:
        page_data = User.query.filter_by(uid=keywords).order_by(
            User.uid.desc()
        ).paginate(page=page, per_page=10)
    else:
        page_data = User.query.order_by(
            User.uid.desc()
        ).paginate(page=page, per_page=10)
    return render_template('admin/userList.html', page_data=page_data)


@bp.route('/adminlist.html')
@admin_login
def adminList():
    adminList = Admin.query.all()
    return render_template('admin/adminList.html', adminList=adminList)


@bp.route('/pie_doughnut.html')
@admin_login
def pie_doughnut():
    data = source.pie_doughnut
    shenqin=Apply.query.filter_by(status='申请中').count()
    shenhe = Apply.query.filter_by(status='审核中').count()
    kaizhan=Apply.query.filter_by(status='开展中').count()
    return render_template('admin/pie_doughnut.html', title=data.title, data=[
        {'name': '申请中', 'value': shenqin},
        {'name': '审核中', 'value': shenhe},
        {'name': '开展中', 'value': kaizhan},

    ], legend=data.legend, unit=data.unit)

@bp.route('/welcome.html')
def welcome():
    return render_template('admin/welcome.html')

@bp.route('/change.html', methods=['GET', 'POST'])
def change():
    if request.method == 'POST':
        uid = request.args.get('customerId')
        print('uid', uid)
        password1 = request.form['passwd']
        password2 = request.form['passwd2']
        user = User.query.filter_by(uid=uid).first()
        passwd = user._password
        msg = check_password_hash(passwd, password1)
        print(msg)
        if password2==password1:
           User.query.filter_by(uid=uid).update({
            '_password': generate_password_hash(password2)
           })
           db.session.commit()
           db.session.close()
        else:
            print('兩次密碼不一致！')
            return render_template('admin/changePasswd.html',msg='密碼不一致')
        return redirect(url_for('admin.userList'))


@bp.route('/changePasswd.html')
def changePasswd():
    uid = request.args.get('customerId')
    users = User.query.filter_by(uid=uid).first()
    username = users.username
    return render_template('admin/changePasswd.html', username=username,id=uid)

@bp.route('/userDel.html')
def userDel():
    id=request.args.get('customerId')
    userList=User.query.filter_by(uid=id).first()
    db.session.delete(userList)
    db.session.commit()
    print('删除成功')
    return redirect(url_for('admin.userList'))

@bp.route('/adminAdd.html', methods=['GET', 'POST'])
def adminAdd():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        passwd=generate_password_hash(password)
        print('pwd:',passwd)
        level = request.form['auth']
        email=request.form['email']
        print('level:',level)
        AdminList = Admin(name=name, _password=passwd,email=email, role=level)
        db.session.add(AdminList)
        db.session.commit()
    else:
        return render_template('admin/adminAdd.html')
    return redirect(url_for('admin.adminList'))

@bp.route('/adminEdit.html')
def adminEdit():
    Id = request.args.get('customerId')
    adminList = Admin.query.filter_by(id=Id).first()
    return render_template('admin/adminEdit.html', adminList=adminList)

@bp.route('/Edit.html', methods=['GET', 'POST'])
def Editadmin():
    if request.method == 'POST':
        id = request.args.get('customerId')
        name = request.form['name']
        email = request.form['email']
        role=request.form['role']
        Admin.query.filter_by(id=id).update({
            'name': name,
            'email': email,
            'role': role
        })
        print('更新成功')
        db.session.commit()
        db.session.close()
        return redirect(url_for('admin.adminEdit'))

@bp.route('/adminDel.html')
def adminDel():
    id=request.args.get('customerId')
    adminList=Admin.query.filter_by(id=id).first()
    db.session.delete(adminList)
    db.session.commit()
    print('删除成功')
    return redirect(url_for('admin.adminList'))

@bp.route('/logout')
@admin_login
def logout():
    session.clear()
    return redirect(url_for('front.login'))