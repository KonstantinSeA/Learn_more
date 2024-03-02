from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, EmailField

from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок новости', validators=[DataRequired()])
    content = TextAreaField('Текст новости', validators=[DataRequired()])
    is_private = BooleanField('Личная новость')
    submit = SubmitField('Применить')
