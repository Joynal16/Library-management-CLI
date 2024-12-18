from save_all_books import save_all_books
import random
import datetime import datetime

def add_books(all_books):
    title = input("enter Book Title")
    author =input("Enter Author Name:")
    year = int(input("Enter Publishing Year number: "))
    price = int(input("enter Books price"))

while True:
    try:
        quantity = int(input("Enter quantity number: "))
        break
    except ValueError:
        print("Invalid a input.Please a enter valid.")

    isbn = random.randint(10000,99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H: %M: %S:")


    book = {
        "title": title,
        "author": author,
        "isbn":  isbn,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Books Added Successfully")

    return all_books