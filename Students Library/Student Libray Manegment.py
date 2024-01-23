class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)

    def finedBook(self, bookname):
        if bookname in self.books:
            print(f"You have been Fined for {bookname} for not returning on time.")
            self.books.remove(bookname)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookname)
        else:
            print("Sorry, this book has already been issued to someone else. Please wait.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book on time.")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["A Brief History of Time", "Cosmos", "The Selfish Gene", "Sapiens: A Brief History of Humankind", "The Double Helix", "The Elegant Universe", "The Immortal Life of Henrietta Lacks", "The Feynman Lectures on Physics", "The Origin of Species", "Guns, Germs, and Steel", "Silent Spring", "The Structure of Scientific Revolutions", "Lab Girl", "Longitude", "Thinking, Fast and Slow", "The Emperor of All Maladies", "The Man Who Knew Infinity", "The Hidden Life of Trees"])

    student = Student()

    while True:
        welcomeMsg = '''======Welcome to Central Library======
        Please choose an option:
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Fine for a book
        5. Exit the Library'''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            book_to_fine = input("Enter the name of the book to fine: ")
            centralLibrary.finedBook(book_to_fine)
        elif a == 5:
            print("Thanks for choosing Central Library! Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")
        print(welcomeMsg)




    








