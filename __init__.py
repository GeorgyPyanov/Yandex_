from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def countdown():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
                      'Присоединяйся!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def ro():
    return f'''<!doctype html>
                <html lang="en">
                  <body>
                  <figure>
                      <h1>Привет, Марс!</h1>
                      <img src="{url_for('static', filename='img/MARS.jpg')}">
                      <figcaption>Жди нас, Марс!</figcaption>
                  </figure>
                  </body>
                </html>'''


@app.route('/sample_file_upload')
def sample_file_upload():
    a = True
    if a:
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                          </head>
                          <body>
                            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="{url_for('static', filename='img/img.png')}" class="d-block w-100">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for('static', filename='img/img_1.png')}" class="d-block w-100">
                                </div>
                                <div class="carousel-item">
                                <img src="{url_for('static', filename='img/img_2.png')}" class="d-block w-100">
                                </div>
                                <div class="carousel-item">
                                <img src="{url_for('static', filename='img/img_3.png')}" class="d-block w-100">
                                </div>
                              </div>
                              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Предыдущий</span>
                              </button>
                              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Следующий</span>
                              </button>
                              <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
                              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
                            </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
