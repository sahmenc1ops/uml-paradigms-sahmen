# Event-Driven Programming
# Library Management System

def borrow_book():
    print("Book borrowing event triggered.")
    print("The book has been borrowed successfully.")

def return_book():
    print("Book return event triggered.")
    print("The book has been returned successfully.")

events = {
    "borrow": borrow_book,
    "return": return_book
}

event = "borrow"

if event in events:
    events[event]()