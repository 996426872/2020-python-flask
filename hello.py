from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!, Have a nice day!This is my first web.</h1>'.format(name.title())


