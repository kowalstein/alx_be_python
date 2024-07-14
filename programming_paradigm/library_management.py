class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
class Library(Book):

    def __init__(self):
        self._books = []
    
    def add_book(self,book):
        if isinstance(book, Book):
            self._books.append(book)
            print (f"Book {book.title} by {book.author} added to library.")
        else:
            print ("Invalid book object. Please provide a valid Book instance.")
    
    def _find_book_index(self,title):
        for index, book in enumerate(self._books):
            if book.title == title:
                return index

    def check_out_book(self, title):
        index = self._find_book_index(title)
        if index is not None:
            if not self._books[index]._is_checked_out:
                self._books[index]._is_checked_out = True
                print (f"{title} checked out successfully.")
            else:
                print (f"{title} is already checked out.")
        else:
            print (f"{title} not found in the library.")

    def return_book(self, title):
        index = self._find_book_index(title)
        if index is not None:
            if self._books[index]._is_checked_out:
                self._books[index]._is_checked_out = False
                print (f"{title} returned successfully.")
            else:
                print (f"{title} is not checked out.")
        else:
            print (f"{title} not found in the library.")

    def list_availble_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
