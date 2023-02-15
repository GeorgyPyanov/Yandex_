from flask import Flask, url_for, request, render_template

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


@app.route('/auto_answer')
@app.route('/answer')
def sample_file_upload():
    param = {'title': '', 'surname': '111', 'name': '', 'education': '', 'profession': '', 'motivation': '', 'ready': ''}
    return render_template('auto_answer.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
