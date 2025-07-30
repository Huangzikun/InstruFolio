from flask import Flask
from app.config import config_by_name
from app.extensions import db, login_manager


def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # 注册蓝图
    from app.obe.routes import obe

    app.register_blueprint(obe)

    # 创建数据库表
    # with app.app_context():
    #     db.create_all()

    return app
