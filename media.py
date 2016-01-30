# Import the webbrowser library
import webbrowser


class Movie():
    # __doc__ =
    """ This class provides a way to store movie related information. """

    VALID_RATINGS = {"G", "PG", "PG-13", "R"}

    # "Function named __init__  initializes or creates
    # space in memory for a new instance of Movie"
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube,
                 initial_release_year, directors, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.initial_release_year = initial_release_year
        self.directors = directors
        self.rating = rating

    # Function show_trailer(self) opens a browser and
    # shows the trailer for the 'self' instance parameter
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
