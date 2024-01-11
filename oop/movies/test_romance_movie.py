from oop.movies.movie import Movie
from oop.movies.romance_movie import RomanceMovie

def test_movie_watch():
    movie = Movie("A walk to remember", 2.0)
    assert movie.watch() == "Watching A walk to remember for 2.0 hours!"

def test_romance_movie_watch():
    romance_movie = RomanceMovie("Pride and Prejudice", 2.5)
    assert romance_movie.watch() == "Watching Pride and Prejudice for 2.5 hours and feeling all warm and fuzzy inside!"

    assert romance_movie.creates_warmth
