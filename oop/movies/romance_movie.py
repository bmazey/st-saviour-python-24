from oop.movies.movie import Movie

class RomanceMovie(Movie):
    """A class which defines all romance movies."""
        # All romance movies have title and duration.Use float for duration
    def __init__(self, title: str, duration: float):
        super().__init__(title, duration)

        # All romance movies create a warm, fuzzy feeling
        self.creates_warmth = True

    # Override the watch method for romance movies
    def watch(self):
        return f"Watching {self.title} for {str(self.duration)} hours and feeling all warm and fuzzy inside!"