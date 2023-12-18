from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello world</h1>'


@app.route(('/new'))
def new():
    return '<h2>This is a new redirect</h2>'


app.run()
