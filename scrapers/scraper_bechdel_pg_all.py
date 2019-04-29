from urllib.request import urlopen
from bs4 import BeautifulSoup
import time #just in case
import csv

#creates column name for csv
column_names=["movie_title", "movie_imdb_url","bechdel_rating"]
file = open("bechdel_movies.csv", 'w', newline='', encoding='utf-8')
#following open csv file and creates column names
writer = csv.writer(file)
writer.writerow(column_names)

#following lines of code establish bechdeltest urls to be scraped
def all_page_scraper(i):

    front_url = "http://bechdeltest.com/?page="
    full_url = front_url + str(i)
    html = urlopen(full_url)
    bs = BeautifulSoup(html, 'html.parser')
    list_all = bs.find('div',{'class': 'list'})
    for movie in list_all.findAll('div',{'class': 'movie'}):
        #BELOW is code that does ACTUAL scraping
        movie_title = movie.get_text()
        film = movie_title.strip("\n")
        #print(movie) #this is a test
        #movie_info.append(movie_title)#adds to the empty list

        movie_imdb_url = movie.find('a')['href']
        #print(movie.find('a')['href']) #this is a test

        movie_bechdel_rating = movie.find('img')['alt'].strip("[[]]") #instead of .strip("[[]]") > you could use [2]
        #print(movie.find('img')['alt'].strip("[[]]")) #this is a test

        movie_info = [film, movie_imdb_url, movie_bechdel_rating]
        print(movie_info)
        writer.writerow(movie_info)
        #print(movie_info)

for i in range(0,38):#test with small amt of pgs first
    all_page_scraper(i)

#file.close()
