from oop.movies.movie import Movie
from oop.movies.fantasy_movie import FantasyMovie

# Test for the Movie class
def test_movie_watch():
    # Create a Movie object
    movie = Movie("Harry Potter", 2.0)
    
    # Check if the watch method provides the expected output
    assert movie.watch() == "Watching Harry Potter for 2.0 hours!"

# Test for the FantasyMovie class
def test_fantasy_movie_watch():
    # Create a FantasyMovie object
    fantasy_movie = FantasyMovie("The Lord of the Rings", 3.5)
    
    # Check if the watch method provides the expected output for fantasy movies
    assert fantasy_movie.watch() == "Watching The Lord of the Rings for 3.5 hours and entering a magical world!"
    
    # Check if the takes_to_magical_world attribute is set to True for fantasy movies
    assert fantasy_movie.takes_to_magical_world

if __name__ == "__main__":
    # Run the tests
    test_movie_watch()
    test_fantasy_movie_watch()
    print("All tests passed!")

