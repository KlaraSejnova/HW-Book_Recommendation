#download data from webpage
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip'
with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall()
#clean data
import pandas
users = pandas.read_csv('BX-Users.csv', sep = ';',encoding='cp1251')
#remove all empty raw
users = users.dropna(how='all')
#remove at the beginning and at the end blank space
users["Location"] = users["Location"].str.strip()
#read Books file
books = pandas.read_csv('BX-Books.csv', sep = ';',encoding='cp1251', escapechar="\\")
books = books.dropna(how='all')
books["Book-Title"] = books["Book-Title"].str.strip()
books["Book-Author"] = books["Book-Author"].str.strip()
#read ratings
ratings = pandas.read_csv('BX-Book-Ratings.csv', sep = ';',encoding='cp1251')
books = books.dropna(how='all')
