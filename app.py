from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/index/')
def hello_index():
    return 'Hello, Index2!'