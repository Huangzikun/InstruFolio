from flask import current_app
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length, ValidationError


class AIQueryForm(FlaskForm):
    """AI查询接口表单，用于接收用户输入的长文本并进行验证"""
    user_text = TextAreaField(
        'user_text',
        validators=[
            DataRequired(message='请输入用户文本'),
            Length(max=10000, message='文本长度10000字符')
        ]
    )

    # 新增可选系统提示词字段
    system_prompt = TextAreaField(
        'system_prompt',
        default="你是桂林学院信息工程学院的一名计算机专任教师，你拥有丰富的教学经验。请根据用户的要求执行处理，最后生成以json格式进行返回",
        validators=[
            Length(max=10000, message='系统提示词长度不能超过10000字符')
        ]
    )

    # 新增：固定密钥校验字段
    access_key = StringField(
        'access_key',
        validators=[
            DataRequired(message='请输入访问密钥'),  # 确保密钥不为空
        ]
    )

    # 新增：自定义验证器，校验密钥是否匹配预设值
    def validate_access_key(self, field):
        # 写死的固定密钥（可根据需求修改为实际密钥）
        FIXED_SECRET_KEY = current_app.config['ACCESS_KEY']
        if field.data != FIXED_SECRET_KEY:
            raise ValidationError('访问密钥无效或已过期')
