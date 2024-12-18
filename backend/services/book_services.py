from models.book_model import books_collection

class BookService:
    def get_all_books(self):
        return list(books_collection.find({}, {"_id": 0}))

    def add_book(self, book_data):
        books_collection.insert_one(book_data)
