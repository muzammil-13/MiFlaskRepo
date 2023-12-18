from flask import Flask

new = Flask(__name__)


@new.route('/profile/muzammil')
def profile():
    return '<h1>This is muzammil</h1>'


@new.route('/profile/<username>')
def profile1(username):
    return '<h2>This profile is for %s </h2>' % username


@new.route('/profile/<int:id>/')
def profile2(id):
    return '<h1>This profile is for %d</h1>' % id


new.run(debug=True)
