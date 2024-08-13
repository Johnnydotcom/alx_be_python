class Book:
    def __init__(self, title, author):
        self.author = author
        self.title = title
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(author, title)
        self.file_size = file_size
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(author, title)
        self.page_count = page_count
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.book = book
        
    def list_books(self):