import unittest
from oop.movies.horror_movie import Horror_movie

class TestMovies(unittest.TestCase):

    def test_movie_watch(self):
        movie = movie("Inception")
        self.assertEqual(movie.watch(), "Watching Inception.")

    def test_horror_movie_watch(self):
        horror_movie = Horror_movie("The Conjuring")
        self.assertEqual(horror_movie.watch(), "Watching The Conjuring and getting scared!")

if __name__ == '__main__':
    unittest.main()