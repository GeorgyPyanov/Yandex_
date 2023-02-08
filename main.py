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


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
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
                            <title>Отбор астронавтов</title>
                            <h1>Анкета претендента</h1>
                            <h5>на участии в миссии</h5>
                          </head>
                          <body>
                            <div>
                                <form class="login_form" method="post">
                                    <input type"" class="form-control" id="name" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                    <div class="form-group">
                                      <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </div>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <label for="about">Какие у вас есть профессии?</label>
                                    <div class="form-group form-check">
                                      <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                      <label class="form-check-label" for="acceptRules">пилот</label>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                      <label class="form-check-label" for="acceptRules">строитель</label>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                      <label class="form-check-label" for="acceptRules">экзобиолог</label>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                      <label class="form-check-label" for="acceptRules">врач</label>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                      <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group form-check">
                                      <label class="form-check-label" for="acceptRules">климатолог</label>
                                      <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')