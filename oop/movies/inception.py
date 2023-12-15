from oop.movies.horror_movie import Horror_Movie

class Inception(Horror_Movie):
    """a class which defines all Slasher"""
    def __init__(self, name):
        super().__init__(name)

if __name__ == "__main__":
    movie = Horror_Movie("Inception")
    print(movie.watch())

    horror_movie = Horror_Movie("The Conjuring")
    print(horror_movie.watch())

    