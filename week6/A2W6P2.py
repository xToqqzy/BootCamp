books = []


def search_book(books, term):
    for book in books:
        if term in book['title'] or term in book['author'] or term in book['publisher']:
            return True
    return False


def main():
    while True:
        action = input("[A] Add book\n[S] Search book\n[E] Exit\n")

        if action == 'A':
            book_details = input("Book details: ").split(',')
            if len(book_details) == 4:
                exists = False
                for book in books:
                    if book['title'] == book_details[0]:
                        exists = True
                        break
                if not exists:
                    books.append({
                        'title': book_details[0],
                        'author': book_details[1],
                        'publisher': book_details[2],
                        'pub_date': book_details[3]
                    })
                    print("Book has been added")
                else:
                    print("This book is already in the collection.")
            else:
                print("Invalid input. Please use: title,author,publisher,year")

        elif action == 'S':
            term = input("Search term: ")
            if search_book(books, term):
                print(f"Found a book for: {term}")
            else:
                print(f"No book found for: {term}")

        elif action == 'E':
            for book in books:
                print(book)
            break

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
