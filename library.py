from datetime import datetime

class Library:
    def __init__(self):
        self.books = {}

    #add book
    def add_book(self, name, author):
        if name in self.books:
            print("Book already exists.")
        else:
            self.books[name] = {
                "author": author,
                "status": "Available",
                "issued_time": None
            }
            print("Book added successfully.")

    # View Books
    def view_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nLibrary Books")
            print("-" * 40)
            for book, info in self.books.items():
                print(f"Book   : {book}")
                print(f"Author : {info['author']}")
                print(f"Status : {info['status']}")
                print("-" * 40)

    # Issue Book
    def issue_book(self, name):
        if name in self.books:
            if self.books[name]["status"] == "Available":
                self.books[name]["status"] = "Issued"
                self.books[name]["issued_time"] = datetime.now()
                print("Book issued successfully.")
            else:
                print("Book already issued.")
        else:
            print("Book not found.")

    # Return Book
    def return_book(self, name):
        if name in self.books:
            if self.books[name]["status"] == "Issued":
                issued_time = self.books[name]["issued_time"]
                return_time = datetime.now()

                days_taken = (return_time - issued_time).days
                fine = 0

                if days_taken > 7:
                    fine = (days_taken - 7) * 50

                self.books[name]["status"] = "Available"
                self.books[name]["issued_time"] = None

                print("Book returned successfully.")
                print(f"Days taken : {days_taken}")
                print(f"Late fine  : ₹{fine}")
            else:
                print("Book was not issued.")
        else:
            print("Book not found.")

    # Delete Book
    def delete_book(self, name):
        if name in self.books:
            del self.books[name]
            print("Book deleted successfully.")
        else:
            print("Book not found.")


# MAIN PROGRAM
library = Library()

while True:
    print("\nLibrary Management System ")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author name: ")
        library.add_book(name, author)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        name = input("Enter book name to issue: ")
        library.issue_book(name)

    elif choice == "4":
        name = input("Enter book name to return: ")
        library.return_book(name)

    elif choice == "5":
        name = input("Enter book name to delete: ")
        library.delete_book(name)

    elif choice == "6":
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
