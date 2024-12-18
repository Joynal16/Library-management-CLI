import save_all_books
from datetime import datetime
def update_books(all_books):
    search_book = input("Enter book Titlr to update: ")
    for book in all_books:
        title = input("enter Book Title")
        author = input("Enter Author Name:")
        year = int(input("Enter Publishing Year number: "))
        price = int(input("enter Books price"))
        quantity = int(input("Enter quantity number: "))

        book_last_update_at  = datetime.now().strftime("%d-%m-%Y %H: %M: %S:")
        book["title"] = title
        book["author"] = author
        book["year"] = year
        book["price"] = price
        book["quantity"] = quantity
        book["bookLastUpdateedAt"] = book_last_update_at

        save_all_books.save_all_books(all_books)
        print("Book updated sucessfully")
        return all_books
    print("Book not found")