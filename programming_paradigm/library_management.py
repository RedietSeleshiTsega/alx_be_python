class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """A class representing the library system."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book with the given title as checked out."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                break

    def return_book(self, title):
        """Mark a book with the given title as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                break

    def list_available_books(self):
        """List all available (not checked out) books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
