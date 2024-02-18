class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def list_books(self):
        with open(self.filename, "r") as file:
            content = file.read()

        if not content:
            print("\nNo books have been added yet.")
        else:
            print("\nBooks:")
            print(content)

    def add_book(self, new_book: str):
        with open(self.filename, "a+") as file:
            file.write(new_book + "\n")
            print("\nBook successfully added to the file.")

    def remove_book(self, book_to_remove: str):
        with open(self.filename, "r") as file:
            books = file.readlines()

        with open(self.filename, "w") as file:
            
            for book in books:
                if book.strip() != book_to_remove:
                    file.write(book)
                
                print(f"\n{book_to_remove} has been removed from the file.")
           

    def __del__(self):
        if self.file and not self.file.closed:
            self.file.close()
            print("\nExiting the program.")


lib = Library()
choice = ""
while True:
    print("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Enter q to Quit\n")

    choice = input("Enter your choice: ")
    if choice == "q":

     break

    
    if choice == "1":
        lib.list_books()

    elif choice == "2":
        new_book = input("\nEnter the name of the book you want to add: ")
        lib.add_book(new_book)
    if choice == "3":

        lib.list_books()

        book_to_remove = input("\nEnter the name of the book you want to remove: ")
        lib.remove_book(book_to_remove)

    if choice not in ["1", "2", "3", "q"]:
        print("Invalid selection. Please use 1, 2, 3, or q.")