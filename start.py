from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

Message = namedtuple('Message', 'text tag username')
messages = []


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']
    username = request.form['username']

    messages.append(Message(text, tag, username))

    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
