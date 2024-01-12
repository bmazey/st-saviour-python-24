from oop.movies.movie import Movie
from oop.movies.comedy_movie import ComedyMovie

# Test for the Movie class
def test_movie_watch():
    # Create a Movie object
    movie = Movie("Dumb and Dumber", 2.0)
    # Check if the watch method provides the expected output
    assert movie.watch() == "Watching Dumb and Dumber for 2.0 hours!"

# Test for the ComedyMovie class
def test_comedy_movie_watch():
    # Create a ComedyMovie object
    comedy_movie = ComedyMovie("Murder Mystery", 1.5)
    # Check if the watch method provides the expected output for comedy movies
    assert comedy_movie.watch() == "Watching Murder Mystery for 1.5 hours and having a good laugh!"
    # Check if the makes_people_laugh attribute is set to True for comedy movies
    assert comedy_movie.makes_people_laugh


