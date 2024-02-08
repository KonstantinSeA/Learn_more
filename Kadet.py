from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '</br>'.join(['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                         'Присоединяйся!'])


@app.route('/image_mars')
def image_mars():
    code = f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/Mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <br>Вот она какая, красная планета</br>
                  </body>
                </html>'''
    return code


@app.route('/promotion_image')
def promotion_image():
    code = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" 
        href="{url_for('static', filename='css/style.css')}" />
        <title>Колонизация</title>
      </head>
      <body>
        <h1>Жди нас, Марс!</h1>
        <br></br>
        <img src="{url_for('static', filename='img/Mars.png')}" 
        alt="здесь должна была быть картинка, но не нашлась">
        <br></br>
        <div class="alert alert-secondary" role="alert">
          Человечество вырастает из детства.
        </div>
        <div class="alert alert-success" role="alert">
          Человечеству мала одна планета.
        </div>
        <div class="alert alert-dark" role="alert">
          Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-warning" role="alert">
          И начнем с Марса!
        </div>
        <div class="alert alert-danger" role="alert">
          Присоединяйся!
        </div>
      </body>
    </html>"""
    return code


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Отбор астронавтов</title>
            </head>
          <body>
            <h1 align="center">Анкета Претендента</h1>
            <h2 align="center">на участие в миссии</h2>
            <div>
              <form class="selection_form" method="post">
                <input type="text" class="form-control" id="surname"
                placeholder="Введите фамилию" name="surname">
                <input type="text" class="form-control" id="name"
                placeholder="Введите имя" name="name">
                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                placeholder="Введите адрес почты" name="email">
                <div class="form-group">
                  <label for="educationSelect">Какое у Вас образование?</label>
                  <select class="form-control" id="educationSelect" name="education">
                    <option>Без образования</option>
                    <option>Начальное</option>
                    <option>Среднее</option>
                    <option>Среднее специальное</option>
                    <option>Незаконченное высшее</option>
                    <option>Законченное высшее</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="form-check">Выберете основную профессию</label>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="work" id="Injener-Searcher" value="Injener-Searcher" checked>
                    <label class="form-check-label" for="Injener-Searcher">Инженер-Исследователь</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="work" id="Injener-Builder" value="Injener-Builder">
                    <label class="form-check-label" for="Injener-Builder">Инженер-Строитель</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="work" id="Pilot" value="Pilot">
                    <label class="form-check-label" for="Pilot">Пилот</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="work" id="Meteorolog" value="Meteorolog">
                    <label class="form-check-label" for="Meteorolog">Метеоролог</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="work" id="Injener-Live" value="Injener-Live">
                    <label class="form-check-label" for="Injener-Live">Инженер по Жизнеобезпечению</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="work" id="Injener-Rad" value="Injener-Rad">
                    <label class="form-check-label" for="Injener-Rad">Инженер по радиационной защите</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="work" id="Doctor" value="Doctor">
                    <label class="form-check-label" for="Doctor">Врач</label>
                  </div>
                </div>
                <div class="form-group">
                  <label for="form-check">Укажите пол</label>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                    <label class="form-check-label" for="male">Мужской</label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                    <label class="form-check-label" for="female">Женский</label>
                  </div>
                </div>
                <div class="form-group">
                  <label for="photo">Приложите фотографию</label>
                  <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <div class="form-group">
                  <label for="motivation">Почему вы желаете принять участие в миссии?</label>
                  <textarea class="form-control" id="motivation" rows="4" name="motivation"></textarea>
                </div>
                <div class="form-group form-check">
                  <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                  <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
              </form>
            </div>
          </body>
        </html>'''
    elif request.method == 'POST':
        print(request.form)
        return "Форма отправлена"


@app.route('/choice/<string:planet_name>')
def choice(planet_name):
    code = f"""
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet" 
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
            crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" 
            href="{url_for('static', filename='css/style.css')}" />
            <title>Колонизация</title>
          </head>
          <body>
            <h1 align="center">Мое предложение: {planet_name.capitalize()}!</h1>
            <div class="alert alert-secondary" role="alert">
              Эта планета близка к Земле;
            </div>
            <div class="alert alert-success" role="alert">
              На ней много необходимых ресурсов;
            </div>
            <div class="alert alert-dark" role="alert">
              На ней есть вода и атмосфера;
            </div>
            <div class="alert alert-warning" role="alert">
              На ней есть небольшое магнитное поле;
            </div>
            <div class="alert alert-danger" role="alert">
              Наконец, она просто красива!
            </div>
          </body>
        </html>"""
    return code


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    code = f"""
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" 
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" 
                href="{url_for('static', filename='css/style.css')}" />
                <title>Колонизация</title>
              </head>
              <body>
                <h1>Результаты отбора</h1>
                <h4>Претендента на участие в миссии {nickname.capitalize()}</h4>
                <div class="alert alert-success" role="alert">
                  Поздравляем! Ваш рейтинг после {str(level)} этапа отбора
                </div>
                <h4>составляет {str(rating)}!</h4>
                <div class="alert alert-warning" role="alert">
                  Желаем удачи!
                </div>
              </body>
            </html>"""
    return code


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
