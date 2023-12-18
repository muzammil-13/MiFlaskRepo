from flask import Flask, render_template

app = Flask(__name__)


@app.route('/books')
def book():
    books = [{'name': ' The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'cover': "https://s26162.pcdn.co/wp-content/uploads/2018/02/gatsby-original2.jpg"},
             {'name': 'Pride and Prejudice', 'author': 'Jane Austen', 'cover': "https://s26162.pcdn.co/wp-content/uploads/2021/10/3b47d124002685f2a3c67e47383232c7.jpg"},
             {'name': 'Brave New World', 'author': 'Aldous Huxley', 'cover': "https://s26162.pcdn.co/wp-content/uploads/2021/10/bravenewworld.jpg"}]
    return render_template('books.html', books=books)


app.run(debug=True)
