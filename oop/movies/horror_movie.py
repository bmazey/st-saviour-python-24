from oop.movies.movie import Movie

class HorrorMovie(Movie):
    """A class which defines all horror movies."""
    def __init__(self, title: str, duration: float):
        super().__init__(title, duration)

        # All horror movies create fear
        self.creates_fear = True

    # Override the watch method for horror movies
    def watch(self):
        return f"Watching {self.title} for {str(self.duration)} hours and getting scaredddd!"