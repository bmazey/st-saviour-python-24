from oop.movies import Movies

class Horror_movie(Movies):
    """a class which defines all Horror_Movies"""
    def __init__(self, name):
        super().__init__(name)
        self.movies = True

class Movie:
    """A base class for all movies."""
    def __init__(self, title):
        self.title = title

    def watch(self):
        return f"Watching {self.title}."

class HorrorMovie(Movie):
    """A class which defines all horror movies."""
    def __init__(self, title):
        super().__init__(title)

        # All horror movies create fear
        self.creates_fear = True

    # Override the watch method for horror movies
    def watch(self):
        return f"Watching {self.title} and getting scared!"
    
    