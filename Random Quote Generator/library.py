"""This code shall perform the basic functions of a library. It shall let users add books, borrow books, return books and see all the available and unavailable books.
"""

def start():
    # Original books in the library
    allBooks = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]

    borrowedISBNs = []

    # Main loop that keeps program going until user exits
    while True:
        printMenu()
        selection = input("Your selection> ").lower()

        # User selection to add new books
        if selection in ['1', 'a']:
            addBook(allBooks)
        # User selection for borrowing books
        elif selection in ['2', 'r']:
            borrowBook(allBooks, borrowedISBNs)
        # User selection for returning books
        elif selection in ['3', 't']:
            returnBook(borrowedISBNs)
        # User selection for listing books
        elif selection in ['4', 'l']:
            listAllBooks(allBooks, borrowedISBNs)
        # User selection for exit
        elif selection in ['5', 'x']:
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            listAllBooks(allBooks, borrowedISBNs)
            break
        # Tells user to fix their input if selection is invalid
        else:
            print("Wrong selection! Please selection a valid option.")


def printMenu():
    # Print the main menu
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')


def addBook(allBooks):
    # Define the function to add New Books
    bookName = input("Book name> ")    # Input for the book name
    # Make sure the book name does not contain any * or % and ask user to re-enter the book name if it does
    while '*' in bookName or '%' in bookName:
        print("Invalid book name!")
        bookName = input("Book name> ")

    # Input for the author's name
    author = input("Author name> ")

    # Input for the edition number and makes sure it is an integer
    while True:
        edition_str = input("Edition> ")
        if edition_str.isdigit():
            edition = int(edition_str)
            break
        else:   # Makes user re-enter edition number if input was not an integer
            print("Please enter a valid edition number.")

    # Input and validate the ISBN
    while True:
        isbn = input("ISBN> ")
        if len(isbn) != 13 or not isbn.isdigit():
            print("Invalid ISBN!")
        elif not isValidISBN(isbn):
            print("ISBN check failed!")
            break
        elif isbn in [book[0] for book in allBooks]:
            print("Duplicate ISBN is found! Cannot add the book.")
        else:
            allBooks.append([isbn, bookName, author, edition, []])
            print("A new book is added successfully.")
            break


def isValidISBN(isbn):
    # Check if the ISBN is valid
    weights = ('1313131313131')
    total = 0
    for i in range(13):
        total += int(weights[i]) * int(isbn[i])
    return total % 10 == 0


def borrowBook(allBooks, borrowedISBNs):
    # Definition for the function to borrow books
    # Input for the borrower's name and the search term
    borrowerName = input("Enter the borrower name> ")
    searchTerm = input("Search term> ")

    # Find available books and make list for matching books
    availableBooks = [book for book in allBooks if book[0] not in borrowedISBNs]
    matchingBooks = []

    # Find books based on the search term
    if searchTerm.endswith('*'):
        matchingBooks = [book for book in availableBooks if searchTerm[:-1].lower() in book[1].lower()]  # If search input has a star at end, check if the word is anywhere in a book's title
    elif searchTerm.endswith('%'):
        matchingBooks = [book for book in availableBooks if book[1].lower().startswith(searchTerm[:-1].lower())] # If search input has a percent sign at end, check if the word is at the start of a book's title
    else:
        matchingBooks = [book for book in availableBooks if searchTerm.lower() == book[1].lower()] # Check if search input matches any book title's exactly

    # Borrows all books that match user's search input
    if matchingBooks:
        for book in matchingBooks:
            book[4].append(borrowerName)  # Adds borrower's name to the borrowed list for the book
            borrowedISBNs.append(book[0])   #Adds book to the borrowed books list
            print(f'-"{book[1]}" is borrowed!')
    else:
        print("No books found!")


def returnBook(borrowedISBNs):
    # Define the function for returning borrowed books
    isbn = input("ISBN> ")  # Input for ISBN
    if isbn in borrowedISBNs:
        book_name = borrowedISBNs[isbn]
        borrowedISBNs.remove(isbn)  # Removes book from borrowed list when returned
        print(f'-"{book_name}" is returned!')
    else:
        print("No book is found in the borrowed books list!")


def listAllBooks(allBooks, borrowedISBNs):
    # List all the books with their availability in format required
    for book in allBooks:
        print("---------------")
        if book[0] in borrowedISBNs:
            print("[Unavailable]")
        else:
            print("[Available]")
        print(f"{book[1]} - {book[2]}")
        print(f"E: {book[3]} ISBN: {book[0]}")
        print(f"Borrowed by: {book[4]}")
    print("---------------")


# Start the program
start()
