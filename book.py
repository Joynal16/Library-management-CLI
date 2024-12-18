

import add_books
import delete_book_file

import view_all_book
import restore_books_file
from datetime import datetime
import update_book_file

all books = []



while True:
    print("Welcome to Library Management system")
    print("0. Exit")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/delete")

    all_books = restore_books_file.restore_all_books(all_books)

    menu = input("select any number")

    if menu == "0":
        print("Thanks for using library Management")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book_file.update_books(all_books)
    elif menu =="4":
        delete_book_file.delete_books(all_books)
    else:
        print("Choose a valid number")