# Procedural Programming

books = ["Python Basics", "UML Guide", "Data Science"]

def display_books():
    for book in books:
        print(book)

def borrow_book(book):
    if book in books:
        books.remove(book)
        print(book, "has been borrowed.")
    else:
        print(book, "is not available.")

display_books()
borrow_book("Python Basics")
display_books()