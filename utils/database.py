import json

"""

All actions with database

"""

books = []


# add the book
def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


# Show book list
def get_books():
    return books


# If book is read
def mark_book_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


# Delete book
def delete_book(name):
    global books

    # add each book to the new list if book['name'] != # name
    books = [book for book in books if book['name'] != name]


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
