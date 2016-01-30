# Import the media file because you will make instances of class Movie
# Import the fresh_tomatoes file to call its function open_movies_page
import media
import fresh_tomatoes


# Create movie objects
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    "1995",
    "John Lasseter",
    "G")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
    "2009",
    "James Cameron",
    "PG-13")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Going back in time to meet authors",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=FAfR8omt-CY",
    "2011",
    "Woody Allen",
    "PG-13")

school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=LqEszt5wG9I",
    "2003",
    "Richard Linklater",
    "PG-13")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk",
    "2007",
    "Brad Bird, Jan Pinkava",
    "G")

hunger_games = media.Movie(
    "Hunger Games",
    "A really real reality show",
    "http://upload.wikimedia.org/wikipedia/en/a/ab/Hunger_games.jpg",
    "https://www.youtube.com/watch?v=4S9a5V9ODuY",
    "2014",
    "Gary Ross, Francis Lawrence",
    "PG-13")

# Create an array called movies and populate it with the movie instances
movies = [toy_story, avatar, midnight_in_paris, school_of_rock,
          ratatouille, hunger_games]

# Call the fresh_tomatoes.py file in order to create the HTML page and call
# the function open_movies_page and pass in the array 'movies' as argument
# in order to open the webpage populated with the movie instances
fresh_tomatoes.open_movies_page(movies)


# The following code can be uncommented for testing purposes
# Each line will print into the IDLE shell the respective information
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)
