import json

"""

All actions with database

"""

books = []


# add the book
def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


# Show book list
def list_book():
    for book in books:
        print(f"Book name: {book['name']}      Book author: {book['author']}     Book read: {book['read']}")


# If book is read
def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


# Delete book
def delete_book(name):
    for book in books:
        if book['name'] == name:
            books.remove(book)


# Load list to file
def load_to_file():
    with open('books_json.txt', 'w') as file:
        json.dump(books, file)


# Read book list from file
def read_from_file():
    with open('books_json.txt', 'r') as file:
        file_contents = json.load(file)
    for book in file_contents:
        print(f"Book name: {book['name']}      Book author: {book['author']}     Book read: {book['read']}")
