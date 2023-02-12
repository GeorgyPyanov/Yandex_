from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def greeting(prof):
    if prof in ['геодезист', 'конструктор', 'сметчик',
                'технолог', 'электроник', 'механик',
                'электрик', 'энергетик', 'строитель',
                'проектировщик', 'испытатель', 'электротехник',
                'теплотехник', 'мехатроник', 'эколог']:
        username = 1
    else:
        username = 0
    return render_template('base.html', username=username)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')