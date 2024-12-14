class Book:
    def __init__(self, title, author, year, isbn, pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}, ISBN: {self.isbn}, Pages: {self.pages}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter year of publication: "))
        isbn = input("Enter book ISBN: ")
        pages = int(input("Enter number of pages: "))
        new_book = Book(title, author, year, isbn, pages)
        self.books.append(new_book)
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def search_book(self):
        search_title = input("Enter book title to search: ")
        found_books = [book for book in self.books if search_title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print("No books found with that title.")

    def menu(self):
        while True:
            print("\nLibrary Menu")
            print("1. Add Book")
            print("2. Display Books")
            print("3. Search Book by Title")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.display_books()
            elif choice == '3':
                self.search_book()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    library = Library()
    library.menu()
