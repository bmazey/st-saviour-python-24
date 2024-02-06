from oop.movies.movie import Movie
from oop.movies.comedy_movie import ComedyMovie

def test_movie_watch():
    # Assert Dumb and Dumber comdey movie is long 2 hours. 
    movie = Movie("Dumb and Dumber", 2.0)
    assert movie.watch() == "Watching Dumb and Dumber for 2.0 hours!"

def test_comedy_movie_watch():
    # Assert Murder Myster comedy movie is long 1 and half hours. 
    comedy_movie = ComedyMovie("Murder mystery", 1.5)
    assert comedy_movie.watch() == "Watching Murder mystery for 1.5 hours and having a good laugh!"

    assert comedy_movie.makes_people_laugh
    # Assert it's true that comedy movies are makes people laugh