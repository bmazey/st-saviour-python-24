from oop.movies.movie import Movie
from oop.movies.horror_movie import HorrorMovie

# Test for the Movie class
def test_movie_watch():
    # Create a Movie object
    movie = Movie("Inception", 2.0)
    # Check if the watch method provides the expected output
    assert movie.watch() == "Watching Inception for 2.0 hours!"

# Test for the HorrorMovie class
def test_horror_movie_watch():
    # Create a HorrorMovie object
    horror_movie = HorrorMovie("The Conjuring", 1.8)
    # Check if the watch method and attribute provide the expected output for horror movies
    assert horror_movie.watch() == "Watching The Conjuring for 1.8 hours and getting scaredddd!"
    assert horror_movie.creates_fear

if __name__ == "__main__":
    # Run the tests
    test_movie_watch()
    test_horror_movie_watch()
    print("All tests passed!")
