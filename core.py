from .utils import track_access, permission_check

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Returns "Title by Author" [cite: 281]
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Returns number of pages [cite: 282]
    def __len__(self):
        return self.pages

    # Compares if two books are identical [cite: 283]
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author


class Library:
    def __init__(self):
        self.books = []

    # Applies the closure and decorator we wrote [cite: 289, 290, 291]
    @permission_check("Admin")
    @track_access
    def add_book(self, user_role, book):
        self.books.append(book)
        print(f"Success: Added '{book.title}' to the library.")

    # Makes the library iterable in a for-loop [cite: 284, 285, 286]
    def __getitem__(self, index):
        return self.books[index]