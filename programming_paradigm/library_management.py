class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute - starts as available

    def check_out(self):

        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):

        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):

        return not self._is_checked_out

    def get_status(self):

        return "Available" if self.is_available() else "Checked Out"


class Library:


    def __init__(self, name="Local Library"):

        self.name = name
        self._books = []

    def add_book(self, title, author):

        new_book = Book(title, author)
        self._books.append(new_book)
        print(f'Added "{title}" by {author} to the library.')
        return new_book

    def add_book_instance(self, book):

        if isinstance(book, Book):
            self._books.append(book)
            print(f'Added "{book.title}" by {book.author} to the library.')
        else:
            print("Error: Only Book instances can be added to the library.")

    def find_book(self, title):

        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title):

        book = self.find_book(title)

        if book is None:
            print(f'Book "{title}" not found in the library.')
            return False

        if book.check_out():
            print(f'Successfully checked out "{book.title}" by {book.author}.')
            return True
        else:
            print(f'"{book.title}" is already checked out.')
            return False

    def return_book(self, title):

        book = self.find_book(title)

        if book is None:
            print(f'Book "{title}" not found in the library.')
            return False

        if book.return_book():
            print(f'Successfully returned "{book.title}" by {book.author}.')
            return True
        else:
            print(f'"{book.title}" was not checked out.')
            return False

    def list_available_books(self):

        available_books = [book for book in self._books if book.is_available()]

        if not available_books:
            print("No books are currently available.")
            return available_books

        print(f"\nAvailable books in {self.name}:")
        print("-" * 40)
        for book in available_books:
            print(f" {book}")

        return available_books

