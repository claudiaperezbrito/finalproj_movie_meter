#scrapes imdb url list
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time #just in case
import csv

#hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
       #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       #'Accept-Encoding': 'none',
       #'Accept-Language': 'en-US,en;q=0.8',
       #'Connection': 'keep-alive'}


#put my urls into one list from txt file
myfile = open('movie.txt')
movie_raw = myfile.readlines()
# now movie_raw holds a list made from lines in states.txt
myfile.close()
# new empty list for clean strings after stripping
movies_urls = []
for url in movie_raw:
    movies_urls.append(url.strip(' \n'))

#test with few urls
mini_list=[]
for i in range(7260,7599):
    mini_list.append(movies_urls[i])

#creates column name for csv
column_names=["movie_name","movie_yr", "movie_directors","movie_writers"]
file = open("imdb_movies_12.csv", 'w', newline='', encoding='utf-8')
#following open csv file and creates column names
writer = csv.writer(file)
writer.writerow(column_names)

#following is function that scrapes the details needed
for url in mini_list:
        html = urlopen(url)#link will be variable
        bs = BeautifulSoup(html, 'html.parser')
        #following is in case of using headers
        #req = session.get(url, headers=hdr)
        #bsObj = BeautifulSoup(req.text, "html5lib")
        mov= bs.find('div',{'class':'title_wrapper'}).find('h1')
        mov_1=(mov.get_text())
        movie_name = (mov_1[0:-8])

#start of year scrape code
        try:
            movie_yr = bs.find('div',{'class': 'title_wrapper'}).find('span', {'id':'titleYear'})
            year = movie_yr.text.strip("()")
            #print(year) #test
        except:
            year = "None"

#start of directors scrape code
        try:
            director_names=[]
            directors = bs.findAll('div',{'class':'credit_summary_item'})[0]
            dir = directors.findAll('a')

            for name in dir:
                person = name.get_text()
                director_names.append(person)
        except:
            director_names = "None"

#start of writers scrape code
        try:
            writer_names=[]
            writers = bs.findAll('div',{'class':'credit_summary_item'})[1]
            writ = writers.findAll('a')


            for name in writ:
                persontwo = name.get_text()
                if "credit" in persontwo or "cast" in persontwo:
                    pass
                else:
                    writer_names.append(persontwo)
        except:
            writer_names = "None"
        time.sleep(1)
        movie_details = [movie_name, year, director_names, writer_names]
        print(movie_details)
        writer.writerow(movie_details)
file.close()
driver.quit();
