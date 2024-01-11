from oop.movies.movie import Movie
from oop.movies.horror_movie import HorrorMovie

def test_movie_watch():
    movie = Movie("Inception", 2.0)
    assert movie.watch() == "Watching Inception for 2.0 hours!"

def test_horror_movie_watch():
    horror_movie = HorrorMovie("The Conjuring", 1.8)
    assert horror_movie.watch() == "Watching The Conjuring for 1.8 hours and getting scaredddd!"

    assert horror_movie.creates_fear