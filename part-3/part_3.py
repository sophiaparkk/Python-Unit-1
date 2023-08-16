
my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}
my_book_2 = {
    "title": "Book A",
    "author": "Author A",
    "year": 1995,
    "rating": 5.00,
    "pages": 412
}
my_book_list = [my_book,my_book_2]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_information(dict):
    book_string = (f"The title of this book is {dict['title']} written by {dict['author']} in {dict['year']}. It has {dict['pages']} pages with a rating of {dict['rating']}.")
    return book_string

print(book_information(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def book_title(dict):
    book_title_return = dict['title']
    return book_title_return

print(book_title(my_book))

def book_author(dict):
    book_author_return = dict['author']
    return book_author_return

print(book_author(my_book))

def book_year(dict):
    book_year_return = dict['year']
    return book_year_return

print(book_year(my_book))

def book_rating(dict):
    book_rating_return = dict['rating']
    return book_rating_return

print(book_rating(my_book))

def book_pages(dict):
    book_pages_return = dict['pages']
    return book_pages_return

print(book_pages(my_book))


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def total_number_pages(list_of_books):
    list_of_pages = []
    for book in list_of_books:
        list_of_pages.append(book['pages'])

    sum_of_pages = sum(list_of_pages)
    return sum_of_pages

print(total_number_pages(my_book_list))

def oldest_book(list_of_books):
    book_years_list = []
    for book in list_of_books:
        book_years_list.append(book['year'])

    oldest_year = book_years_list[0]
    for year in book_years_list:
        if year < oldest_year:
            oldest_year = year
            return(oldest_year)

print(oldest_book(my_book_list))

                                                                                           