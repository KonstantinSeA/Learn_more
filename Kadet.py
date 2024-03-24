from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main_page():
    return "А программа живет на /carousel"


@app.route('/index')
def index():
    return "А программа живет на /carousel"


@app.route('/carousel')
def astronaut_selection():
    return f"""
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
            <title>Пейзажи Марса</title>
        </head>
        <body>
            <h1 style="text-align: center">Результаты отбора</h1>
            <div id="carouselExample" class="carousel slide">
                <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src={url_for('static', filename='img/Mars_1.jpg')} 
                          class="d-block w-100" alt="МММ Ошибочка">
                    </div>
                    <div class="carousel-item">
                        <img src={url_for('static', filename='img/Mars_2.jpg')} 
                          class="d-block w-100" alt="МММ Ошибочка">
                    </div>
                    <div class="carousel-item">
                        <img src={url_for('static', filename='img/Mars_3.jpg')} 
                          class="d-block w-100" alt="МММ Ошибочка">
                    </div>
                </div>
                <button class="carousel-control-prev" type="button" 
                  data-bs-target="#carouselExample" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" 
                  data-bs-target="#carouselExample" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
            </div>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
