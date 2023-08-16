### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def add_book():
#     title = input("What is your most interesting book? " )
#     author = input("Who is the author of this book? ")
#     year = input("What year was this book published? ")
#     rating = input("What would you rate this book out of 5? Up to two decimal points ")
#     pages = input("How many pages are in this book? ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(add_book())


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def add_book_v2():
#     title = input("What is your most interesting book? " )
#     author = input("Who is the author of this book? ")
#     year = int(input("What year was this book published? "))
#     rating = float(input("What would you rate this book out of 5? Up to two decimal points "))
#     pages = int(input("How many pages are in this book? "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

# print(add_book_v2())



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def add_book_v2():
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


    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary
    

print(add_book_v2())





### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

book1 = {
        "title": 'me',
        "author": 'me',
        "year": 1995,
        "rating": 4.5,
        "pages": 270
}

book2 = {
        "title": 'him',
        "author": 'him',
        "year": 1993,
        "rating": 5.0,
        "pages": 300
}

book3 = {
        "title": 'you',
        "author": 'you',
        "year": 2023,
        "rating": 3.5,
        "pages": 230
}

list_of_books = [book1, book2, book3]

# def main_menu():
#     options = int(input("Main menu:\n1.Add a new book\n2.See all books on shelf\nChoose 1 or 2 "))
#     if options == 1:
#         new_book = add_book_v2()
#         list_of_books.append(new_book)
#         print(list_of_books)
#     elif options == 2:
#         print(list_of_books)
#     else:
#         print('1 or 2 was not chosen. Back to Main Menu')

# main_menu()

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu():
    options = int(input("Main menu:\n1.Add a new book\n2.See all books on shelf\nChoose 1 or 2. Press 0 to leave main menu. "))
    if options == 1:
        new_book = add_book_v2()
        list_of_books.append(new_book)
        print(list_of_books)
    elif options == 2:
        print(list_of_books)
    elif options == 0:
        exit()
    else:
        print('1 or 2 was not chosen. Back to main menu.')
    
    while options != 0:
        main_menu()

main_menu()