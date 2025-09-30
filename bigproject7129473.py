# Library Management System
class library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lenddict = {}

    def displaybooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendbook(self, user, book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book: user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")

    def addbook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the book list")

    def returnbook(self, book):
        self.lenddict.pop(book)
        print("Book has been returned")

if __name__ == "__main__":
    books = library(['Python', 'How to make an OS', 'Science', 'Assembly'], 'CodeWithArham')
    while True:
        print(f"\nWelcome to the {books.name} library. Enter your choice to continue:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.displaybooks()
        elif user_choice == 2:
            user = input("Enter your name: ")
            book = input("Enter the name of the book: ")
            books.lendbook(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            books.addbook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            books.returnbook(book)

        print("Press 'q' to quit and 'c' to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
