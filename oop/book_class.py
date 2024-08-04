class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def __str__(self):
        print(f"(title) by (author), published in (year)")
        
    def __del__(self):
        print(f"Book '{self.title}' by {self.author} is being deleted.")
    