"""
Author= sahil
"""
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def mark_as_borrowed(self):
        self.available = False

    def mark_as_available(self):
        self.available = True

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.author} - {'Available' if self.available else 'Borrowed'}"


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_available()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s Borrowed Books:")
            for book in self.borrowed_books:
                print(book)
        else:
            print(f"{self.name} has no borrowed books.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                print(book)
        else:
            print("No books available.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


def menu():
    print("Library Management System Menu")
    print("1. List Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. List Borrowed Books")
    print("5. Add a Book to Library")
    print("6. Exit")


def main():
    # Initialize the library and add books
    library = Library()
    library.add_book(Book("Mitti da Bawa ", "Harbhajan Sing", 2008))
    library.add_book(Book(" Puran singh", "Bhai Vir Singh", 1999))
    library.add_book(Book("Gaddar", "Kuldeep Salil", 2008))

    # Initialize patrons
    patrons = {
        "Alice": Patron("Alice"),
        "Bob": Patron("Bob")
    }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library.list_books()
        elif choice == "2":
            customer_name = input("Enter your name: ").strip()
            book_title = input("Enter book title to borrow: ").strip()
            customer = patrons.get(customer_name)
            book = library.find_book(book_title)
            if customer and book:
                customer.borrow_book(book)
            elif not customer:
                print("Customer not found.")
            elif not book:
                print("Book not found.")
        elif choice == "3":
            customer_name = input("Enter your name: ").strip()
            book_title = input("Enter book title to return: ").strip()
            customer = patrons.get(customer_name)
            book = library.find_book(book_title)
            if customer and book:
                customer.return_book(book)
            elif not customer:
                print("Customer not found.")
            elif not book:
                print("Book not found.")
        elif choice == "4":
            customer_name = input("Enter your name: ").strip()
            customer = patrons.get(customer_name)
            if customer:
                customer.list_borrowed_books()
            else:
                print("Customer not found.")
        elif choice == "5":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = int(input("Enter book year: ").strip())
            library.add_book(Book(title, author, year))
            print(f"Book '{title}' added to the library.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
