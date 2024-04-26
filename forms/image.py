from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

from wtforms.validators import DataRequired


class ImageForm(FlaskForm):
    file = FileField('Добавить Фото', validators=[DataRequired()])
    submit = SubmitField('Отправить')
