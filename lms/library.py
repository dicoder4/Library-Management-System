from lms.database import Database
from lms.book import Book
from lms.user import User

class Library:
    def __init__(self):
        self.db = Database()

    def create_tables(self):
        self.db.create_tables()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        query = "INSERT INTO books (title, author, isbn, available) VALUES (?, ?, ?, ?)"
        self.db.execute_query(query, (book.title, book.author, book.isbn, book.available))

    def register_user(self, name):
        user = User(name)
        query = "INSERT INTO users (name) VALUES (?)"
        self.db.execute_query(query, (user.name,))

    def borrow_book(self, user_id, isbn):
        book_query = "SELECT * FROM books WHERE isbn = ? AND available = 1"
        book = self.db.fetch_one(book_query, (isbn,))
        if book:
            book_id = book[0]
            query = "INSERT INTO transactions (user_id, book_id, status) VALUES (?, ?, ?)"
            self.db.execute_query(query, (user_id, book_id, 'borrowed'))
            update_query = "UPDATE books SET available = 0 WHERE id = ?"
            self.db.execute_query(update_query, (book_id,))
            print(f"User {user_id} borrowed the book {isbn}")
        else:
            print("Book is not available")

    def return_book(self, user_id, isbn):
        book_query = "SELECT * FROM books WHERE isbn = ?"
        book = self.db.fetch_one(book_query, (isbn,))
        if book:
            book_id = book[0]
            query = "UPDATE books SET available = 1 WHERE id = ?"
            self.db.execute_query(query, (book_id,))
            update_query = "UPDATE transactions SET status = 'returned' WHERE user_id = ? AND book_id = ?"
            self.db.execute_query(update_query, (user_id, book_id))
            print(f"User {user_id} returned the book {isbn}")
        else:
            print("Book not found")
