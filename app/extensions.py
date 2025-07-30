from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
# 初始化扩展，不直接绑定app
db = SQLAlchemy()
login_manager = LoginManager()
cors = CORS()
