from flask import Flask, render_template
from flask_wtf import CSRFProtect

from apps.front import bp as front_bp
from apps.admin import bp as admin_bp
from exts import db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(front_bp)
    app.register_blueprint(admin_bp)
    app.config.from_object('config')
    CSRFProtect(app)
    db.init_app(app)
    return app

if __name__ == '__main__':
    app=create_app()
    app.run(host='127.0.0.1',port=8000,debug=True)
