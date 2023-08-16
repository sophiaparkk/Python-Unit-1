### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

# with open("library.txt", "w") as f:
#     f.write("title, author, year, rating, pages\n")

# with open("library.txt", "r") as f:
#     print(f.read())

# with open("library.txt", "a") as f:
#     f.write("title, author, year, rating, pages\n")

# with open("library.txt", "r") as f:
#     print(f.read())

# def book_library():
#     title = input("What is your most interesting book? " )
#     author = input("Who is the author of this book? ")
#     try:
#         year = int(input("What year was this book published? "))
#     except:
#         year = int(input("Please enter the year in yyyy number format "))
#     try:
#         rating = float(input("What would you rate this book out of 5? "))
#     except:
#         rating = float(input("Please enter a number with a decimal point"))
#     try:
#         pages = int(input("How many pages are in this book? "))
#     except:
#         pages = int(input("Please enter a the number of pages in whole number format"))

#     with open("library.txt", "a") as f:
#         f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

# book_library()





### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

# def show_all__books():
#     with open("library.txt") as f:
#         read_lines = f.readlines()
#         # print(f.readlines())

#         for line in read_lines:
#             line = line.split(", ") #we have to delimit these lines because they are coming in as strings and not as a list of a list

#             book_dictionary = {
#                 "title": line[0],
#                 "author": line[1],
#                 "year": line[2],
#                 "rating": line[3],
#                 "pages": line[4]
#             }

#             print(book_dictionary)

# show_all__books()


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

#JUST TOOK THIS CODE FROM MY PART 4 SO NAMES MAY NOT QUITE WORK
# def main_menu():
#     options = int(input("Main menu:\n1.Add a new book\n2.See all books on shelf\nChoose 1 or 2. Press 0 to leave main menu. "))
#     if options == 1:
#         new_book = add_book_v2()
#         list_of_books.append(new_book)
#         print(list_of_books)
#     elif options == 2:
#         print(list_of_books)
#     elif options == 0:
#         exit()
#     else:
#         print('1 or 2 was not chosen. Back to main menu.')
    
#     while options != 0:
#         main_menu()

# if __name__ == '__main__':
#     main_menu()



### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def add_book():
    title = input("What is your most interesting book? " )
    author = input("Who is the author of this book? ")
    try:
        year = int(input("What year was this book published? "))
    except:
        year = int(input("Please enter the year in yyyy number format "))
    try:
        rating = float(input("What would you rate this book out of 5? "))
    except:
        rating = float(input("Please enter a number with a decimal point"))
    try:
        pages = int(input("How many pages are in this book? "))
    except:
        pages = int(input("Please enter a the number of pages in whole number format"))

    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

def show_all__books():
    with open("library.txt") as f:
        read_lines = f.readlines()
        # print(f.readlines())

        for line in read_lines:
            line = line.split(", ") #we have to delimit these lines because they are coming in as strings and not as a list of a list

            book_dictionary = {
                "title": line[0],
                "author": line[1],
                "year": line[2],
                "rating": line[3],
                "pages": line[4]
            }

            print(book_dictionary)


def main_menu():
    options = int(input("Main menu:\n1.Add a new book\n2.See all books on shelf\nChoose 1 or 2. Press 0 to leave main menu. "))
    if options == 1:
        add_book()
        print('Book added!')
    elif options == 2:
        show_all__books()
    elif options == 0:
        exit()
    else:
        print('1 or 2 was not chosen. Back to main menu.')
    
    while options != 0:
        main_menu()

if __name__ == '__main__':
    main_menu()