from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    """搜索表单"""
    query = StringField('搜索内容', validators=[DataRequired(), Length(1, 100)])
    submit = SubmitField('搜索')
