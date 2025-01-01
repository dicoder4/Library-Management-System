from flask import Flask, render_template, request, redirect, url_for
from lms.database import Database
from lms.library import Library

app = Flask(__name__)

library = Library()

@app.route('/')
def index():
    # Fetch all books from the database
    db = Database()
    books = db.fetch_all("SELECT * FROM books")
    db.close()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        library.add_book(title, author, isbn)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/register_user', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        name = request.form['name']
        library.register_user(name)
        return redirect(url_for('index'))
    return render_template('register_user.html')

if __name__ == '__main__':
    app.run(debug=True)
