# Object-Oriented Programming
# Library Management System

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is not available.")

    def return_book(self):
        self.available = True
        print(self.title, "has been returned.")


book = Book("Python Basics")

book.borrow()
book.return_book()