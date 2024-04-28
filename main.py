from flask import Flask, render_template
import json
import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index_page():
    title = 'Не та страница'
    return render_template('base.html', title=title)


@app.route('/member')
def carousel():
    with open('templates/users.json', mode='r', encoding='utf-8') as file:
        users = json.load(file)
    member = users[random.choice(list(users.keys()))]
    return render_template('member.html', title=member['name'], member=member, sorted=sorted)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
