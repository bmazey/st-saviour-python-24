from oop.movies.movie import Movie
from oop.movies.romance_movie import RomanceMovie

# Test for the Movie class
def test_movie_watch():
    # Create a Movie object
    movie = Movie("A Walk to Remember", 2.0)
    # Check if the watch method provides the expected output
    assert movie.watch() == "Watching A Walk to Remember for 2.0 hours!"

# Test for the RomanceMovie class
def test_romance_movie_watch():
    # Create a RomanceMovie object
    romance_movie = RomanceMovie("Pride and Prejudice", 2.5)
    # Check if the watch method and attribute provide the expected output for romance movies
    assert romance_movie.watch() == "Watching Pride and Prejudice for 2.5 hours and feeling all warm and fuzzy inside!"
    assert romance_movie.creates_warmth

if __name__ == "__main__":
    # Run the tests
    test_movie_watch()
    test_romance_movie_watch()
    print("All tests passed!")

