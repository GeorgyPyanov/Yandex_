from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username1 = StringField('id капитана', validators=[DataRequired()])
    password1 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


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


@app.route('/auto_answer', methods=['GET', 'POST'])
@app.route('/answer', methods=['GET', 'POST'])
def sample_file_upload():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('auto_answer.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
