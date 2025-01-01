def validate_isbn(isbn):
    """Validate the ISBN format (simple validation)."""
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False

def format_book_info(book):
    """Format book information for displaying."""
    return f"{book['title']} by {book['author']} (ISBN: {book['isbn']})"

def validate_user_name(name):
    """Validate the user's name to ensure it's not empty."""
    if name and len(name) > 1:
        return True
    return False
