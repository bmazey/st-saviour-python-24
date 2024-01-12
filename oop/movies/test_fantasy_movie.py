from oop.movies.movie import Movie
from oop.movies.fantasy_movie import FantasyMovie

def test_movie_watch():
    # Assert Harry Potter movie is long 2 hours long.
    movie = Movie("Harry Potter", 2.0)
    assert movie.watch() == "Watching Harry Potter for 2.0 hours!"

def test_fantasy_movie_watch():
    # Assert The Lord of the Rings movie is long 3 and half hours long. 
    fantasy_movie = FantasyMovie("The Lord of the Rings", 3.5)
    assert fantasy_movie.watch() == "Watching The Lord of the Rings for 3.5 hours and entering a magical world!"

    assert fantasy_movie.takes_to_magical_world
    # assert it's true that fantasy movies takes to magical world
