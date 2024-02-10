from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main_page():
    return "А программа живет на /load_image"


@app.route('/index')
def index():
    return "А программа живет на /load_image"


@app.route('/load_image', methods=['POST', 'GET'])
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
                <div class="form-group">
                  <label for="photo">Приложите фотографию</label>
                  <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
              </form>
            </div>
          </body>
        </html>'''
    elif request.method == 'POST':
        print(request.form)
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
                        <div class="form-group">
                          <label for="photo">Приложите фотографию</label>
                          <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                        <img src="{dir(request.form['file'])}" 
                         width="427" height="427"
                         alt="здесь должна была быть картинка, но не нашлась">
                        <button type="submit" class="btn btn-primary">Отправить</button>
                      </form>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
