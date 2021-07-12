import pandas
from recommend_me import recommend_me, read_files

ratings, books = read_files()
books_in_list = books["Book-Title"].tolist()
while True:
    #input book
    input_book = input('Input your book and we recommend you a new one to read or press enter to quit! ')
    #title in lowercase
    input_book = input_book.lower()
    if not input_book:
        exit()
    elif input_book in books_in_list:
        print('Lets find you a new book')
        #call the function which finds the book: recommend_me(reader_book,rating), rating is a rating of the book to be recommended
        recommend_me(input_book, ratings, books)
    else:
        print('Your book is not in our database.')
