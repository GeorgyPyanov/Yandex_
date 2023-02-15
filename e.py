from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<username>')
@app.route('/index/<username>')
def greeting(username):
    return render_template('base.html',
                           username=username)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')