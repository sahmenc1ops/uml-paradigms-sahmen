# Functional Programming
# Library Management System

books = [
    "Python Basics",
    "UML Guide",
    "Data Science",
    "Cybersecurity"
]

def available_books(book_list):
    return list(filter(lambda book: book != "Python Basics", book_list))

result = available_books(books)

print("Available books:")
for book in result:
    print("-", book)