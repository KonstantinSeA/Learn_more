from flask import Flask, url_for, render_template
from forms.image import ImageForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/index')
def index_page():
    title = 'Не та страница'
    return render_template('base.html', title=title)


@app.route('/carousel', methods=['GET', 'POST'])
def carousel():
    form = ImageForm()
    files = os.listdir('static/img')
    if form.validate_on_submit():
        f = form.file.data
        if not (f.filename.endswith('.jpg') or f.filename.endswith('.png')):
            return render_template('carousel.html', title='Карусель', files=files,
                                   message='Выбранный Файл Не Фото', form=form)
        f.save(f'static/img/{f.filename}')
        return render_template('carousel.html', title='Карусель', files=files,
                               message='Фото Добавлено', form=form)
    return render_template('carousel.html', title='Карусель', files=files,
                           form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
