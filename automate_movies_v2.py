"""
marylesbirel@gmail.com
10/28/2015

File scrapes recent movie releases from IMDB.com and displays individual
movie information into an organized, local website

Data for each movie includes original fresh_tomatoes requirements:
Movie title, trailer link, movie image

New additions to the file include:
Hover over for movie summary, movie duration

"""

# Imports ordered by standard, related third party, local
import re
from lxml import html
import requests
import fresh_tomatoes_edited
import media

# Define a variable page to call on website where movie info is held.
page=requests.get("http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1")

# Define variable tree to save html website data into a string.
tree = html.fromstring(page.text)

# Below section scrapes information to fill into the movie function.
# Each list is created and often edited to clean the data.

# Movie input 1: movie_list
# Define empty variable movie_list to grab all movie names on IMDB website.
movie_list = []

# Movie names are held within "poster shadowed" class in the HTML.
for el in tree.xpath('//img[contains(@class,"poster shadowed")]'):
    x = el.xpath('@title') # Return the movie title from within the class
    x = ([x.replace(' (2015)', '') for x in x]) # Remove the year from movie title
    movie_list.append(x) # Use the append function to add new movie titles


# Movie input 2: summary
summary = tree.xpath('//div[@itemprop="description"]/text()')
summary_2 = []

# Turn summary variable into a list of list to be consistent
for i in range(len(summary)):
    x = summary[i]
    summary_2.append(x)

# Movie input 3: image_list
# Repeated above method to gain a list of image files from the HTML.
image_list = []
for el in tree.xpath('//img[contains(@class,"poster shadowed")]'):
    x = el.xpath('@src')
    image_list.append(x)


# Movie input 4: trailer_list
# Repeated above method to gain a list of trailer urls from the HTML.
trailer_list = []
for el in tree.xpath('//td[contains(@class,"overview-bottom")]/a'):
    x = el.xpath('@href')
    trailer_list.append(x)

# Cleans trailer_list as above method returned unnecessary elements in list
# Need to strip everything after the ? mark
trailer_list = [s for s in trailer_list if 'video' in str(s)]
for i in range(len(trailer_list)):
   trailer_list[i][0] = re.sub('\?ref_=inth_ov_vi$', '', trailer_list[i][0])
   trailer_list[i][0]  = 'http://www.imdb.com/' + trailer_list[i][0] + '/imdb/embed?autoplay=true'

# Movie input 4: movie_time
movie_time = tree.xpath('//time[@itemprop="duration"]/text()')

# Define var merge which uses the zip function to merge equal length
# lists into individual lists. This function will separate the inputs
# gathered above based on type of variable and instead shuffle strings
# so they are matched based on movie. So each part of list will get
# a movie title, movie summary, move image and so on.
merge = zip(movie_list, summary_2, image_list, trailer_list, movie_time)

# Create var movies.
# This var applies the movie class to each individual movie group provided
# above. TODO: explain what is going on here better.
movies = []

for i in range(len(merge)):
     x = media.Movie(merge[i][0][0],
                         "'" + merge[i][1]+ "'",
                         merge[i][2][0],
                         merge[i][3][0],
                         "Duration: " + merge[i][4]
                         )
     movies.append(x)

# Call on operation to open a website and display the information gathered
# from movies var above.
fresh_tomatoes_edited.open_movies_page(movies)
