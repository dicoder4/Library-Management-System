from lms.library import Library

def main():
    library = Library()
    library.create_tables()
    
    # Example: Add a book and a user
    library.add_book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    library.register_user("John Doe")
    
    # Borrow and return a book (assume a user with ID 1 exists)
    library.borrow_book(1, "9780316769488")
    library.return_book(1, "9780316769488")

if __name__ == "__main__":
    main()
