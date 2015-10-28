"""
marylesbirel@gmail.com
10/28/2015

Creates a class to store unique information about each movie, including
title, summary, movie image, trailer url and duration of movie

"""

## Create a class for movie to store unique information about each movie
## Things to remember: Plan is to store title, storyline, poster_image, imdb_trailer in the class
## Things to do: show_trailer()
## self points to toy story
import webbrowser

class Movie():
    """Creates a class to store unique information about each movie.

    Attributes:
        movie_title: string of movie name
        movie_storyline: string of movie summary
        poster_image: string of .jpg link to movie box image
        trailer_imdb: string of link to imdb movie trailer
        movie_duration: string of movie length
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_imdb, movie_duration):
        """Inits Movie class with attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_imdb_url = trailer_imdb
        self.duration = movie_duration

## each instance method starts with self
    def show_trailer(self):
        """Performs operation to open web browser to play movie trailer."""
        webbrowser.open(self.trailer_imdb_url)
    
