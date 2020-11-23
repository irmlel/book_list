from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'f' to add list to file
- 'o' to load list from file
- 'q' to quit

Your choice:"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            book_name = input('Enter book name: ')
            book_author = input('Enter book author: ')
            database.add_book(book_name, book_author)
            user_input = input(USER_CHOICE)
        elif user_input == 'l':
            database.list_book()
            user_input = input(USER_CHOICE)
        elif user_input == 'r':
            book_name = input('Enter book name: ')
            database.read_book(book_name)
            user_input = input(USER_CHOICE)
        elif user_input == 'd':
            book_name = input('Enter book name: ')
            database.delete_book(book_name)
            user_input = input(USER_CHOICE)
        elif user_input == 'f':
            database.load_to_file()
            user_input = input(USER_CHOICE)
        elif user_input == 'o':
            database.read_from_file()
            user_input = input(USER_CHOICE)


menu()

# def prompt_add_book()  ask for book name and author
# def list_books()  show all the books in our list
# def prompt_read_book() ask for book name and change it to "read" in our list
# def prompt_delete_book() ask for book name and remove book from list
