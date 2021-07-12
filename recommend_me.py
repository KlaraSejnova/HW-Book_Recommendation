import pandas

def read_files(book_file = 'BX-Books.csv',book_ratings_file = 'BX-Book-Ratings.csv'):
    """function which reads the files"""
    #read and clean data
    #read Books file, seperator is ;, coding cp1251 due to russian letter, escapechar - wrong line 6542 - confused by backslash
    books = pandas.read_csv(book_file, sep = ';',encoding='cp1251', escapechar="\\")
    books = books.dropna(how='all')
    #string in lowercase
    books["Book-Title"] = books["Book-Title"].str.lower()
    books["Book-Author"] = books["Book-Author"].str.lower()
    #remove at the beginning and at the end blank space
    books["Book-Title"] = books["Book-Title"].str.strip()
    books["Book-Author"] = books["Book-Author"].str.strip()
    #read and clean data
    #read ratings
    ratings = pandas.read_csv(book_ratings_file, sep = ';',encoding='cp1251')
    ratings = ratings.dropna(how='all')
    return ratings, books


def recommend_me(reader_book, ratings, books, prefered_rating = 10):
    """function which at first reads the database and then search recommended book on the basis of the readers book"""
    #at first join tables
    #ratings_users = pandas.merge(users,ratings)
    all_information = pandas.merge(ratings,books)

    #find user who reads reader_book
    input_book_rating = all_information.loc[all_information['Book-Title'] == reader_book]
    #only those who rate reader_book by high 
    high_ratings = input_book_rating.loc[input_book_rating["Book-Rating"] >= prefered_rating]
    users_in_list = high_ratings["User-ID"].tolist()
    new_book = all_information.loc[all_information["User-ID"].isin(users_in_list)]
    #we found readers who read your book now we will found what else they read
    #only book with the rate higher or equal to the value and recommended book is not the same as the input book 
    new_book = new_book.loc[(new_book["Book-Rating"] >= prefered_rating) & (new_book["Book-Title"] != reader_book)]
    #from the highest prefered_rating
    new_book = new_book.sort_values(["Book-Rating"], ascending=False)
    #is there any book several times?
    new_book_count = new_book["Book-Title"].value_counts()
    new_book_count_dict = new_book_count.to_dict()
    new_book_count_dict = sorted(new_book_count_dict.items(), key=lambda t:t[1], reverse = True)
    #list of recommended book with the value how many times were rated by number 10
    list_of_rec_book = [book_count[0] for book_count in new_book_count_dict][:10]
    new_book = new_book[new_book["Book-Title"].isin(list_of_rec_book)]
    #make a table of 10 most recommended books
    new_book = new_book.drop_duplicates(["Book-Title"])
    new_book.set_index("Book-Title")
    print(new_book[["Book-Title","Book-Author"]])
