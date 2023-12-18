from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/inmakes')
def profile():
    return render_template('profile.html')


@app.route('/profile/<username>')
def profile1(username):
    return render_template('profile.html', username=username,isActive=True)


app.run(debug=True)
