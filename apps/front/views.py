import datetime
import os
from functools import wraps

from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.utils import secure_filename

import config
from apps.front.forms import LoginForm, RegisterForm, ApplyForm
from apps.front.models import User, Apply, Record
from exts import db

bp = Blueprint("front", __name__, url_prefix='/front')


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        user_id = session.get(config.FRONT_CUSTOMER_ID)
        print("session:", user_id)
        if not user_id:
            return redirect(url_for('front.login'))
        else:
            return func(*args, **kwargs)

    return inner


@bp.route('/main.html')
def index():
    keywords = request.args.get('keywords', '', type=str)
    page = request.args.get('page', 1, type=int)
    num = Apply.query.count()
    if keywords:
        page_data = Apply.query.filter(Apply.id == keywords).order_by(
            Apply.applyDate.desc()
        ).paginate(page=page, per_page=3)
    else:
        page_data = Apply.query.order_by(
            Apply.applyDate.desc()
        ).paginate(page=page, per_page=3)
        a = int(3/num)
    return render_template('front/index.html', page_data=page_data, nu=a)


@bp.route('/apply.html')
@login_required
def single():
    return render_template('front/submit.html')


@bp.route('/contact.html')
@login_required
def contact():
    return render_template('front/contact.html')


@bp.route('/detail.html')
def detail():
    id=request.args.get('ApplyId')
    info=Apply.query.filter_by(id=id).first()
    print('info:',info)
    return render_template('front/detail.html',info=info)


@bp.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('front/login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            user = request.form.get('username')

            pwd = request.form.get('password')

            users = User.query.filter_by(username=user).first()
            print(users)
            if users:
                if user == users.username:
                    session[config.FRONT_CUSTOMER_NAME] = users.username
                    session[config.FRONT_CUSTOMER_ID] = users.uid
                    return redirect(url_for('front.index'))
                else:
                    error = "用户名或密码错误!"
                    return render_template('front/login.html')
            else:
                return render_template('front/login.html')
        else:
            return render_template('front/login.html')


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('front.index'))


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('front/register.html')
    if request.method == 'POST':
        if request.method == 'GET':
            return render_template('front/register.html')
        if request.method == 'POST':
            form = RegisterForm(request.form)
            username = form.username.data
            password1 = form.password1.data
            password2 = form.password2.data
            phone = form.phone.data
            if password1 != password2:
                print('两次密码不一致')
            else:
                user = User(username=username, password=password1, phone=phone
                            )
                db.session.add(user)
                db.session.commit()
            return redirect(url_for('front.login'))


@bp.route('/apply.html', methods=['POST'])
@login_required
def apply():
    if request.method == 'POST':
        name = request.form['name']
        user = Apply.query.filter_by(name=name).first()
        if not user:
            tearm = request.form['tearm']
            cost = request.form['cost']
            applyId = session.get(config.FRONT_CUSTOMER_ID)
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f = request.files.get("xiangmu_pic")
            if not f:
                return render_template('front/submit.html', message1='未上传成功！'), 500
            basepath = os.path.dirname(__file__)
            upload_path = os.path.join(basepath, '../../static/front/images/', secure_filename(f.filename))
            f.save(upload_path)
            upload_img = '/static/front/images/' + secure_filename(f.filename)
            print('upload_img:', upload_img)
            zip = request.files.get("xiangmu_zip")
            if not zip:
                return render_template('front/submit.html', message2='未上传成功!'), 500
            upload_zip = os.path.join(basepath, '../../static/front/zips/', secure_filename(zip.filename))
            zip.save(upload_zip)
            upload_zip = 'static/front/zips/' + secure_filename(zip.filename)
            print('upload_zip:', upload_zip)
            content = request.form['message']
            apply = Apply(
                applyId=applyId,
                name=tearm,
                cost=cost,
                level='0',
                applyDate=now,
                img=upload_img,
                zip=upload_zip,
                content=content,
            )
            db.session.add(apply)
            db.session.commit()
            return render_template('front/submit.html', message='上传成功！')


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG', 'PNG', 'bmp', 'zip', 'rar'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


bp.send_file_max_age_default = datetime.timedelta(seconds=1)


@bp.route('/jindu.html')
@login_required
def jindu():
    userId=session.get(config.FRONT_CUSTOMER_ID)
    data=Apply.query.filter_by(applyId=userId).first()
    status=data.status
    list=['申请中','审核中','开展','项目完成','项目归档']
    position=list.index(status)
    print(position)
    p=position
    recordList=Record.query.filter(Record.userId==userId).order_by(Record.addDate.desc()).all()
    print(recordList)
    return render_template('front/jindu.html',recordList=recordList,p=p)


@bp.route('/huibao.html')
@login_required
def huibao():
    return render_template('front/huibao.html')

@bp.route('/AddRecord.html',methods=['POST'])
def addRecord():
    if request.method=='POST':
        userId=session.get(config.FRONT_CUSTOMER_ID)
        content=request.form['message']
        print('content:',content)
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record=Record(
            userId=userId,
            content=content,
            addDate=now
        )
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('front.index'))