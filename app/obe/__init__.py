from flask import Blueprint

# 创建main蓝图，url_prefix可选，若设置则该蓝图下所有路由自动添加前缀
obe = Blueprint('obe', __name__, template_folder='obe', url_prefix='/obe')

# 导入路由模块，避免循环导入
from app.obe import routes