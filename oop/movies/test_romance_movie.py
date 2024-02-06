from oop.movies.movie import Movie
from oop.movies.romance_movie import RomanceMovie

def test_movie_watch():
    # Assert A Walk To Remember movie is long 2 hours long.
    movie = Movie("A walk to remember", 2.0)
    assert movie.watch() == "Watching A walk to remember for 2.0 hours!"

def test_romance_movie_watch():
    # Assert Pride and Prejudice movie is long 2 and half hours long.
    romance_movie = RomanceMovie("Pride and Prejudice", 2.5)
    assert romance_movie.watch() == "Watching Pride and Prejudice for 2.5 hours and feeling all warm and fuzzy inside!"

    assert romance_movie.creates_warmth
    # Assert it's true that romance movie creates warmth. 
