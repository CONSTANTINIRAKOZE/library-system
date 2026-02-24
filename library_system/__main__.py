from .core import Book, Library

# Duck Typing Test: Accepts ANY object with a title [cite: 305]
def borrow_item(item):
    try:
        print(f"Successfully borrowed: {item.title}")
    except AttributeError:
        print("Error: This item cannot be borrowed because it has no title.")

class Magazine:
    def __init__(self, title):
        self.title = title

def main():
    print("--- Booting up the Smart Library System ---")
    my_library = Library()
    book1 = Book("Python Crash Course", "Eric Matthes", 544)
    book2 = Book("Clean Code", "Robert C. Martin", 464)
    
    # Testing access control: Admin works, Guest is denied [cite: 291]
    my_library.add_book("Admin", book1)
    my_library.add_book("Guest", book2)

    print("\n--- Books in Library ---")
    for book in my_library:
        print(book) 

    print("\n--- Duck Typing Test ---")
    my_magazine = Magazine("Wired - March 2026")
    
    borrow_item(book1)       
    borrow_item(my_magazine) 

if __name__ == "__main__":
    main()