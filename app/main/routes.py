from flask import jsonify

from app.main.forms import AIQueryForm
from . import main  # 导入蓝图
from flask import request

from ..tools.Doubao import Doubao


@main.route('/ai/query', methods=['POST'])
def ai_query():
    # 初始化表单（支持JSON和表单数据提交）
    form = AIQueryForm(data=request.get_json() or request.form)

    # 验证表单数据
    if not form.validate():
        return jsonify({
            'success': False,
            'error': '输入无效',
            'details': form.errors  # 返回具体验证错误
        }), 400

    # 获取验证通过的文本（处理前后空格）
    input_text = form.user_text.data.strip()
    system_prompt = form.system_prompt.data.strip()

    doubao = Doubao()
    result = doubao.query(input_text, system_prompt)

    return jsonify({
        'message': 'success',
        'result': result
    })