from flask import Flask
from app.config import config_by_name
from app.extensions import db, login_manager, cors


def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # 配置 CORS（允许前端域名访问，及携带 Cookie）
    cors.init_app(app,
                  origins="http://127.0.0.1:5001",
                  supports_credentials=True,
                  allow_headers=["Content-Type", "X-CSRFToken", "csrf_token"]
                  )

    # 初始化扩展
    db.init_app(app)

    # 注册蓝图
    from app.main import main as main_blueprint
    from app.obe import obe as obe_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(obe_blueprint)

    # 创建数据库表
    # with app.app_context():
    #     db.create_all()

    return app
