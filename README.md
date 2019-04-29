# Gender Movie Meter

This app was created as a final project for the Advanced Web Apps Course at the University of Florida. 

There's a debate about the fact  that films lack female representation, and it's argued that one of the reasons for this is a lack of females in behind the scenes roles. The app permits a user to search for a movie to see the Bechdel Test rating and then get to see the individuals in the director and writer roles.

## How was it done?

Python was used to scrape 7,599 films from 2019-1945 on the Bechdel Test Site (http://bechdeltest.com/), the film's corresponding IMDb links, and the film's 'Bechdel Rating' into a csv. Then the films IMDb links were placed into a txt file to then go into each link and scrape the film's name, release year, director(s), and writer(s), which was written into a csv.

The data was cleaned using excel and then Flask was used to create the app (i.e search feature, index of movies, result page, and each movie page).

### Problems and solutions

Some IMDb links in the Bechdel site were wrong, so when the scraper was running on each IMDb link sometimes it would stop. This is why I had to go manually a paste the correct link for the movie and then start the scraper again from the last movie it left off on (using the range in the scraper). This explains the multiple csv files in the additional csv folder. All those csv were then manually joined into one csv.

